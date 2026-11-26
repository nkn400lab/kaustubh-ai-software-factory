import { test, expect } from '@playwright/test';
import { existsSync } from 'node:fs';

const pages = ['index.html','ai-workbench.html','code-studio.html','test-repair-lab.html','windows-build-kit.html','github-file-sync.html','autonomous-agent.html','package-builder.html'];
test('factory pages exist', async () => { for (const p of pages) expect(existsSync(p), p).toBeTruthy(); });
test('dashboard loads and title is present', async ({ page }) => {
 await page.goto('http://127.0.0.1:4173/index.html');
 await expect(page).toHaveTitle(/.+/);
 await expect(page.locator('body')).not.toBeEmpty();
});
test('all factory pages render without page errors', async ({ page }) => {
 const errors=[]; page.on('pageerror', e=>errors.push(e.message));
 for (const p of pages) { await page.goto('http://127.0.0.1:4173/'+p); await expect(page.locator('body')).not.toBeEmpty(); }
 expect(errors, errors.join('\n')).toEqual([]);
});
