const resultsEl = document.getElementById('results');
const statusEl  = document.getElementById('status');
const btnHeadlines = document.getElementById('btn-headlines');
const searchForm = document.getElementById('search-form');
const searchInput = document.getElementById('search-input');
const countrySelect = document.getElementById('country-select');

function setStatus(msg) { statusEl.textContent = msg || ''; }
function articleCard(a) {
  const img = a.urlToImage || ''; const title = a.title || 'No title';
  return `<article class="card">${img ? `<img src="${img}" alt="">` : ''}<div class="card-content"><h3>${title}</h3><a href="${a.url}" target="_blank">Read more →</a></div></article>`;
}
function renderArticles(articles) { resultsEl.innerHTML = articles.map(articleCard).join(''); }
async function fetchJSON(url) { const res = await fetch(url); if (!res.ok) throw new Error(await res.text()); return res.json(); }
async function loadHeadlines() { const country = countrySelect.value; setStatus('Loading...'); try { const data = await fetchJSON(`/api/top-headlines?country=${country}`); renderArticles(data.articles); setStatus(`Showing ${data.articles.length} headlines`);} catch(e){setStatus('Error');}}
async function doSearch(q) { setStatus(`Searching ${q}...`); try { const data = await fetchJSON(`/api/search?q=${encodeURIComponent(q)}`); renderArticles(data.articles); setStatus(`Found ${data.articles.length} results`);} catch(e){setStatus('Error');}}
btnHeadlines.addEventListener('click', loadHeadlines);
searchForm.addEventListener('submit', e => { e.preventDefault(); const q = searchInput.value.trim(); if(q) doSearch(q); });
window.addEventListener('DOMContentLoaded', loadHeadlines);
