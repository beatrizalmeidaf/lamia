from bs4 import BeautifulSoup
import requests
import os

if not os.path.exists('books'):
    os.makedirs('books')

while True:
    page = 1
    
    stars_dict = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five'}
    
    try:
        stars = int(input('Deseja buscar um livro que possui quantas estrelas (1-5)?\n'))
        if stars not in range(1, 6):
            print("Por favor, insira um número entre 1 e 5.")
            continue
            
        input_star = stars_dict.get(stars)
        
        with open(f'books/{stars}.txt', 'a') as f:
            for num in range(49):
                website = f'https://books.toscrape.com/catalogue/page-{page}.html'
                try:
                    response = requests.get(website)
                    response.raise_for_status()  
                    soup = BeautifulSoup(response.content, 'lxml')
                    
                    books = soup.find_all('article', class_='product_pod')
                    found_books = False
                    
                    for book in books:
                        star_rating = book.find('p', class_='star-rating')['class'][1]
                        stock = book.find('i', class_='icon-ok')
                        
                        if star_rating == input_star and stock is not None:
                            title = book.h3.a['title']
                            price = book.find('p', class_='price_color').text
                            f.write(f'Título: {title}, Preço: {price}, Estrelas: {stars} estrelas\n')
                            found_books = True
                            print(f"Found and saved: {title}")
                    
                    if not found_books:
                        print(f"No books with {stars} stars found on page {page}")
                        
                    page += 1
                    
                except requests.RequestException as e:
                    print(f"Error fetching page {page}: {e}")
                    break
                    
        print(f"\nScraping complete. Results saved to books/{stars}.txt")
        
        continue_scraping = input("\nDeseja procurar mais livros? (s/n): ").lower()
        if continue_scraping != 's':
            break
            
    except ValueError:
        print("Por favor, insira um número válido.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")