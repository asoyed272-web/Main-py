<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>English to Rohingya Dictionary</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            background: linear-gradient(135deg, #1a472a 0%, #2d5a3d 50%, #1a472a 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        .container {
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
            width: 100%;
            max-width: 900px;
            padding: 40px;
        }

        .header {
            text-align: center;
            margin-bottom: 35px;
        }

        .header h1 {
            color: #1a472a;
            font-size: 2.5em;
            margin-bottom: 10px;
        }

        .header-subtitle {
            color: #2d5a3d;
            font-size: 1.1em;
            margin-bottom: 5px;
        }

        .header-desc {
            color: #999;
            font-size: 0.95em;
        }

        .search-container {
            display: flex;
            gap: 10px;
            margin-bottom: 30px;
            flex-wrap: wrap;
        }

        .search-box {
            flex: 1;
            min-width: 200px;
        }

        input[type="text"] {
            width: 100%;
            padding: 15px;
            border: 2px solid #e0e0e0;
            border-radius: 10px;
            font-size: 1em;
            transition: all 0.3s;
        }

        input[type="text"]:focus {
            outline: none;
            border-color: #2d5a3d;
            box-shadow: 0 0 0 3px rgba(45, 90, 61, 0.1);
        }

        input[type="text"]::placeholder {
            color: #ccc;
        }

        .search-buttons {
            display: flex;
            gap: 10px;
        }

        .btn {
            padding: 15px 25px;
            border: none;
            border-radius: 10px;
            cursor: pointer;
            font-size: 0.95em;
            font-weight: bold;
            transition: all 0.3s;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }

        .btn-search {
            background: linear-gradient(135deg, #2d5a3d 0%, #1a472a 100%);
            color: white;
        }

        .btn-search:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 20px rgba(45, 90, 61, 0.3);
        }

        .btn-clear {
            background: #f8f9fa;
            color: #666;
            border: 2px solid #e0e0e0;
        }

        .btn-clear:hover {
            background: #ffe0e0;
            border-color: #ff6b6b;
            color: #ff6b6b;
        }

        .filters {
            display: flex;
            gap: 8px;
            margin-bottom: 25px;
            flex-wrap: wrap;
        }

        .filter-btn {
            padding: 8px 16px;
            border: 2px solid #e0e0e0;
            background: white;
            color: #666;
            border-radius: 8px;
            cursor: pointer;
            font-size: 0.9em;
            font-weight: 600;
            transition: all 0.3s;
        }

        .filter-btn:hover {
            border-color: #2d5a3d;
            color: #2d5a3d;
        }

        .filter-btn.active {
            background: #2d5a3d;
            color: white;
            border-color: #2d5a3d;
        }

        .stats {
            display: flex;
            justify-content: space-around;
            margin-bottom: 25px;
            padding: 15px;
            background: #f8f9fa;
            border-radius: 10px;
            flex-wrap: wrap;
            gap: 20px;
        }

        .stat {
            text-align: center;
        }

        .stat-number {
            font-size: 1.8em;
            font-weight: bold;
            color: #2d5a3d;
        }

        .stat-label {
            font-size: 0.85em;
            color: #999;
            margin-top: 5px;
        }

        .results-container {
            max-height: 600px;
            overflow-y: auto;
            margin-bottom: 20px;
        }

        .result-item {
            background: #f8f9fa;
            padding: 20px;
            border-radius: 12px;
            margin-bottom: 15px;
            border-left: 4px solid #2d5a3d;
            transition: all 0.3s;
            animation: slideIn 0.3s ease;
        }

        @keyframes slideIn {
            from {
                opacity: 0;
                transform: translateY(-10px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .result-item:hover {
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
            transform: translateX(5px);
        }

        .result-english {
            font-size: 1.3em;
            font-weight: bold;
            color: #2d5a3d;
            margin-bottom: 8px;
        }

        .result-rohingya {
            font-size: 1.2em;
            color: #1a472a;
            margin-bottom: 8px;
            font-weight: 600;
        }

        .result-category {
            display: inline-block;
            background: #2d5a3d;
            color: white;
            padding: 4px 12px;
            border-radius: 6px;
            font-size: 0.8em;
            margin-right: 8px;
            margin-bottom: 8px;
        }

        .result-pronunciation {
            font-size: 0.9em;
            color: #666;
            font-style: italic;
            margin-bottom: 8px;
        }

        .result-example {
            font-size: 0.9em;
            color: #555;
            padding: 8px 12px;
            background: white;
            border-left: 3px solid #2d5a3d;
            margin-top: 10px;
            border-radius: 4px;
        }

        .result-actions {
            display: flex;
            gap: 8px;
            margin-top: 12px;
        }

        .btn-favorite {
            padding: 6px 12px;
            background: #fff3cd;
            color: #856404;
            border: 1px solid #ffeaa7;
            border-radius: 6px;
            cursor: pointer;
            font-size: 0.8em;
            transition: all 0.3s;
        }

        .btn-favorite:hover {
            background: #ffeaa7;
        }

        .btn-favorite.added {
            background: #ffc107;
            color: white;
        }

        .btn-copy {
            padding: 6px 12px;
            background: #e7f3ff;
            color: #004085;
            border: 1px solid #b8daff;
            border-radius: 6px;
            cursor: pointer;
            font-size: 0.8em;
            transition: all 0.3s;
        }

        .btn-copy:hover {
            background: #cfe2ff;
        }

        .empty-state {
            text-align: center;
            padding: 40px 20px;
            color: #999;
        }

        .empty-state-icon {
            font-size: 3em;
            margin-bottom: 10px;
        }

        .empty-state-text {
            font-size: 1.1em;
        }

        .favorites-section {
            background: #f8f9fa;
            padding: 20px;
            border-radius: 10px;
            margin-top: 30px;
        }

        .favorites-section h2 {
            color: #2d5a3d;
            margin-bottom: 15px;
            font-size: 1.3em;
        }

        .favorites-list {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
            gap: 10px;
        }

        .favorite-tag {
            background: #2d5a3d;
            color: white;
            padding: 10px;
            border-radius: 8px;
            text-align: center;
            font-size: 0.9em;
            cursor: pointer;
            transition: all 0.3s;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .favorite-tag:hover {
            background: #1a472a;
        }

        .favorite-tag .remove {
            cursor: pointer;
            font-weight: bold;
            margin-left: 5px;
        }

        ::-webkit-scrollbar {
            width: 8px;
        }

        ::-webkit-scrollbar-track {
            background: #f1f1f1;
            border-radius: 10px;
        }

        ::-webkit-scrollbar-thumb {
            background: #2d5a3d;
            border-radius: 10px;
        }

        ::-webkit-scrollbar-thumb:hover {
            background: #1a472a;
        }

        @media (max-width: 768px) {
            .container {
                padding: 20px;
            }

            .header h1 {
                font-size: 2em;
            }

            .search-container {
                flex-direction: column;
            }

            .search-buttons {
                width: 100%;
            }

            .btn-search, .btn-clear {
                flex: 1;
            }

            .results-container {
                max-height: 400px;
            }

            .stats {
                gap: 10px;
            }

            .stat-number {
                font-size: 1.5em;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🌍 English to Rohingya Dictionary</h1>
            <div class="header-subtitle">Learn Rohingya Language</div>
            <div class="header-desc">Search and discover translations, phonetics, and examples</div>
        </div>

        <div class="search-container">
            <div class="search-box">
                <input 
                    type="text" 
                    id="searchInput" 
                    placeholder="Search English word..."
                    autocomplete="off"
                >
            </div>
            <div class="search-buttons">
                <button class="btn btn-search" onclick="searchWord()">🔍 Search</button>
                <button class="btn btn-clear" onclick="clearSearch()">✕ Clear</button>
            </div>
        </div>

        <div class="filters">
            <button class="filter-btn active" onclick="filterByCategory('all')">All Categories</button>
            <button class="filter-btn" onclick="filterByCategory('greetings')">Greetings</button>
            <button class="filter-btn" onclick="filterByCategory('common')">Common</button>
            <button class="filter-btn" onclick="filterByCategory('food')">Food</button>
            <button class="filter-btn" onclick="filterByCategory('family')">Family</button>
            <button class="filter-btn" onclick="filterByCategory('education')">Education</button>
        </div>

        <div class="stats">
            <div class="stat">
                <div class="stat-number" id="totalWords">0</div>
                <div class="stat-label">Total Words</div>
            </div>
            <div class="stat">
                <div class="stat-number" id="searchCount">0</div>
                <div class="stat-label">Results Found</div>
            </div>
            <div class="stat">
                <div class="stat-number" id="favoriteCount">0</div>
                <div class="stat-label">Favorites</div>
            </div>
        </div>

        <div class="results-container" id="resultsContainer"></div>

        <div class="favorites-section">
            <h2>⭐ My Favorites</h2>
            <div class="favorites-list" id="favoritesList">
                <div style="color: #999; padding: 20px; text-align: center;">No favorites yet. Add some!</div>
            </div>
        </div>
    </div>

    <script>
        const dictionary = [
            // Greetings
            { english: 'Hello', rohingya: 'আ��ালামু আলাইকুম', category: 'greetings', pronunciation: 'assalamu alaikum' },
            { english: 'Good morning', rohingya: 'সুপ্রভাত', category: 'greetings', pronunciation: 'su-prabhat' },
            { english: 'Good evening', rohingya: 'সন্ধ্যা বেলা শুভো', category: 'greetings', pronunciation: 'sandhya bela shubo' },
            { english: 'Thank you', rohingya: 'ধন্যবাদ', category: 'greetings', pronunciation: 'dhanyabad' },
            { english: 'Welcome', rohingya: 'স্বাগতম', category: 'greetings', pronunciation: 'swagotom' },
            { english: 'Goodbye', rohingya: 'বিদায়', category: 'greetings', pronunciation: 'biday' },
            { english: 'How are you', rohingya: 'আপনি কেমন আছেন?', category: 'greetings', pronunciation: 'apni kemon achen' },
            { english: 'I am fine', rohingya: 'আমি ভালো আছি', category: 'greetings', pronunciation: 'ami balo achi' },

            // Common words
            { english: 'Yes', rohingya: 'হাঁ', category: 'common', pronunciation: 'ha' },
            { english: 'No', rohingya: 'না', category: 'common', pronunciation: 'na' },
            { english: 'Water', rohingya: 'পানি', category: 'common', pronunciation: 'pani' },
            { english: 'Fire', rohingya: 'আগুন', category: 'common', pronunciation: 'agun' },
            { english: 'Air', rohingya: 'বাতাস', category: 'common', pronunciation: 'batas' },
            { english: 'Earth', rohingya: 'মাটি', category: 'common', pronunciation: 'mati' },
            { english: 'Sun', rohingya: 'সূর্য', category: 'common', pronunciation: 'surya' },
            { english: 'Moon', rohingya: 'চাঁদ', category: 'common', pronunciation: 'chond' },
            { english: 'Night', rohingya: 'রাত', category: 'common', pronunciation: 'rat' },
            { english: 'Day', rohingya: 'দিন', category: 'common', pronunciation: 'din' },

            // Food
            { english: 'Rice', rohingya: 'চাউল', category: 'food', pronunciation: 'chaul' },
            { english: 'Bread', rohingya: 'রুটি', category: 'food', pronunciation: 'ruti' },
            { english: 'Meat', rohingya: 'মাংস', category: 'food', pronunciation: 'manus' },
            { english: 'Fish', rohingya: 'মাছ', category: 'food', pronunciation: 'mach' },
            { english: 'Milk', rohingya: 'দুধ', category: 'food', pronunciation: 'dudh' },
            { english: 'Fruit', rohingya: 'ফল', category: 'food', pronunciation: 'fol' },
            { english: 'Vegetable', rohingya: 'সবজি', category: 'food', pronunciation: 'shobzi' },
            { english: 'Salt', rohingya: 'লবণ', category: 'food', pronunciation: 'lobon' },
            { english: 'Sugar', rohingya: 'চিনি', category: 'food', pronunciation: 'chini' },
            { english: 'Spice', rohingya: 'মশলা', category: 'food', pronunciation: 'moshla' },

            // Family
            { english: 'Father', rohingya: 'বাবা', category: 'family', pronunciation: 'baba' },
            { english: 'Mother', rohingya: 'মা', category: 'family', pronunciation: 'ma' },
            { english: 'Sister', rohingya: 'বোন', category: 'family', pronunciation: 'bon' },
            { english: 'Brother', rohingya: 'ভাই', category: 'family', pronunciation: 'bhai' },
            { english: 'Son', rohingya: 'ছেলে', category: 'family', pronunciation: 'chele' },
            { english: 'Daughter', rohingya: 'মেয়ে', category: 'family', pronunciation: 'meye' },
            { english: 'Grandfather', rohingya: 'দাদা', category: 'family', pronunciation: 'dada' },
            { english: 'Grandmother', rohingya: 'দাদী', category: 'family', pronunciation: 'dadi' },
            { english: 'Uncle', rohingya: 'চাচা', category: 'family', pronunciation: 'chacha' },
            { english: 'Aunt', rohingya: 'চাচী', category: 'family', pronunciation: 'chachi' },

            // Education
            { english: 'School', rohingya: 'স্কুল', category: 'education', pronunciation: 'school' },
            { english: 'Teacher', rohingya: 'শিক্ষক', category: 'education', pronunciation: 'shikshok' },
            { english: 'Student', rohingya: 'শিক্ষার্থী', category: 'education', pronunciation: 'shiksharthi' },
            { english: 'Book', rohingya: 'বই', category: 'education', pronunciation: 'boi' },
            { english: 'Pen', rohingya: 'কলম', category: 'education', pronunciation: 'kolom' },
            { english: 'Paper', rohingya: 'কাগজ', category: 'education', pronunciation: 'kagoj' },
            { english: 'Desk', rohingya: 'ডেস্ক', category: 'education', pronunciation: 'desk' },
            { english: 'Chair', rohingya: 'চেয়ার', category: 'education', pronunciation: 'cheyor' },
            { english: 'Classroom', rohingya: 'শ্রেণী কক্ষ', category: 'education', pronunciation: 'shrenee kokh' },
            { english: 'Education', rohingya: 'শিক্ষা', category: 'education', pronunciation: 'shiksha' },
        ];

        let favorites = JSON.parse(localStorage.getItem('rohingyaFavorites')) || [];
        let currentFilter = 'all';
        let searchResults = [];

        function initializeApp() {
            updateStats();
            renderFavorites();
            displayInitialMessage();
        }

        function displayInitialMessage() {
            const container = document.getElementById('resultsContainer');
            container.innerHTML = `
                <div class="empty-state">
                    <div class="empty-state-icon">📖</div>
                    <div class="empty-state-text">Start by searching for an English word or browsing by category</div>
                </div>
            `;
        }

        function searchWord() {
            const input = document.getElementById('searchInput').value.trim().toLowerCase();
            
            if (!input) {
                displayInitialMessage();
                updateStats();
                return;
            }

            searchResults = dictionary.filter(word => {
                const matchesSearch = word.english.toLowerCase().includes(input) || 
                                     word.rohingya.includes(input);
                const matchesFilter = currentFilter === 'all' || word.category === currentFilter;
                return matchesSearch && matchesFilter;
            });

            renderResults();
            updateStats();
        }

        function renderResults() {
            const container = document.getElementById('resultsContainer');

            if (searchResults.length === 0) {
                container.innerHTML = `
                    <div class="empty-state">
                        <div class="empty-state-icon">🔍</div>
                        <div class="empty-state-text">No words found. Try a different search.</div>
                    </div>
                `;
                return;
            }

            container.innerHTML = searchResults.map(word => `
                <div class="result-item">
                    <div class="result-english">${escapeHtml(word.english)}</div>
                    <div class="result-rohingya">${word.rohingya}</div>
                    <div>
                        <span class="result-category">${word.category.toUpperCase()}</span>
                    </div>
                    <div class="result-pronunciation">📢 ${word.pronunciation}</div>
                    <div class="result-actions">
                        <button class="btn-favorite ${isFavorite(word.english) ? 'added' : ''}" 
                                onclick="toggleFavorite('${word.english}', '${word.rohingya}')">
                            ${isFavorite(word.english) ? '⭐ Added' : '☆ Favorite'}
                        </button>
                        <button class="btn-copy" onclick="copyToClipboard('${word.rohingya}')">
                            📋 Copy
                        </button>
                    </div>
                </div>
            `).join('');
        }

        function filterByCategory(category) {
            currentFilter = category;
            document.querySelectorAll('.filter-btn').forEach(btn => {
                btn.classList.remove('active');
     
