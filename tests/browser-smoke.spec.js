import { test, expect } from '@playwright/test';
import { existsSync, readdirSync } from 'node:fs';

const pages = readdirSync('.').filter(name => name.toLowerCase().endsWith('.html')).sort();

test('all root HTML pages exist', async () => {
  expect(pages.length).toBeGreaterThan(0);
  for (const file of pages) expect(existsSync(file), file).toBeTruthy();
});

test('main dashboard loads', async ({ page }) => {
  await page.goto('http://127.0.0.1:4173/index.html');
  await expect(page).toHaveTitle(/.+/);
  await expect(page.locator('body')).not.toBeEmpty();
});

test('every factory page renders without uncaught page errors', async ({ page }) => {
  const errors = [];
  page.on('pageerror', error => errors.push(`${new URL(page.url()).pathname}: ${error.message}`));
  for (const file of pages) {
    const response = await page.goto('http://127.0.0.1:4173/' + encodeURIComponent(file));
    expect(response && response.ok(), file + ' should return HTTP 200').toBeTruthy();
    await expect(page.locator('body'), file).not.toBeEmpty();
  }
  expect(errors, errors.join('\\n')).toEqual([]);
});
