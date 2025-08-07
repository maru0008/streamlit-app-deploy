books = []
members = []
borrow_records = []

def add_book(book_id, title, author, copies):
    if any(book["book_id"] == book_id for book in books):
        print(f"図書ID「{book_id}」の本は既に存在します。")
        return
    books.append({
        "book_id": book_id,
        "title": title,
        "author": author,
        "copies": copies,
        "available_copies": copies
    })
    print(f"図書「{title}」（ID: {book_id}, 著者: {author}, 冊数: {copies}）を追加しました。")

def list_books():
    if not books:
        print("現在、登録されている図書はありません。")
        return
    print("--- 図書一覧 ---")
    for book in books:
        print(f"ID: {book['book_id']}, タイトル: {book['title']}, 著者: {book['author']}, 総冊数: {book['copies']}, 在庫: {book['available_copies']}")

def search_book():
    book_id = input("検索する図書IDを入力してください: ")
    book = next((b for b in books if b["book_id"] == book_id), None)
    if book:
        print(f"ID: {book['book_id']}, タイトル: {book['title']}, 著者: {book['author']}, 総冊数: {book['copies']}, 在庫: {book['available_copies']}")
    else:
        print(f"図書ID「{book_id}」の本は存在しません。")

def add_member(member_id, name):
    if any(member["member_id"] == member_id for member in members):
        print(f"会員ID「{member_id}」の会員は既に存在します。")
        return
    members.append({"member_id": member_id, "name": name})
    print(f"会員「{name}」（ID: {member_id}）を追加しました。")

def list_members():
    if not members:
        print("現在、登録されている会員はいません。")
        return
    print("--- 会員一覧 ---")
    for member in members:
        print(f"ID: {member['member_id']}, 名前: {member['name']}")

def borrow_book(book_id, member_id):
    book = next((b for b in books if b["book_id"] == book_id), None)
    if not book:
        print(f"図書ID「{book_id}」の本は存在しません。")
        return
    member = next((m for m in members if m["member_id"] == member_id), None)
    if not member:
        print(f"会員ID「{member_id}」の会員は存在しません。")
        return
    if book["available_copies"] <= 0:
        print(f"図書「{book['title']}」は現在貸出可能な冊数がありません。")
        return
    record_count = sum(1 for record in borrow_records if record["member_id"] == member_id and not record["returned"])
    if record_count >= 5:
        print(f"貸出可能数は5冊までです。")
        return
    borrow_records.append({
        "book_id": book_id,
        "member_id": member_id,
        "borrow_date": "2024-11-24",
        "due_date": "2024-12-01",
        "returned": False
    })
    book["available_copies"] -= 1
    print(f"図書「{book['title']}」を会員「{member['name']}」に貸し出しました。\n返却期限: 2024-12-01")

def list_borrowed_books():
    print("--- 貸出中の図書一覧 ---")
    borrow_list = [
        record for record in borrow_records if not record["returned"]
    ]
    if not borrow_list:
        print("現在、貸出中の図書はありません。")
        return
    for record in borrow_list:
        book = next((b for b in books if b["book_id"] == record["book_id"]), None)
        member = next((m for m in members if m["member_id"] == record["member_id"]), None)
        print(f"図書: {book['title']}（ID: {record['book_id']}）, 会員: {member['name']}（ID: {record['member_id']}）, 貸出日: {record['borrow_date']}, 返却期限: {record['due_date']}")

def return_book(book_id, member_id):
    record = next((r for r in borrow_records if r["book_id"] == book_id and r["member_id"] == member_id and not r["returned"]), None)
    if not record:
        print(f"図書ID「{book_id}」本を会員ID「{member_id}」の会員は借りていません。")
        return
    record["returned"] = True
    book = next((b for b in books if b["book_id"] == book_id), None)
    if book:
        book["available_copies"] += 1
        print(f"図書「{book['title']}」が返却されました。")
    else:
        print(f"図書ID「{book_id}」の本は存在しません。")

def calculate_fines():
    print("--- 延滞料金一覧 ---")
    borrow_list = [
        record for record in borrow_records if not record["returned"]
    ]
    if not borrow_list:
        print("現在、貸出中の図書はありません。")
        return
    for record in borrow_list:
        book = next((b for b in books if b["book_id"] == record["book_id"]), None)
        member = next((m for m in members if m["member_id"] == record["member_id"]), None)
        due_date = "2024-12-01"
        today = "2024-12-24"
        overdue_days = max((int(today[-2:]) - int(due_date[-2:])), 0)
        fine = overdue_days * 100
        print(f"図書: {book['title']}（ID: {record['book_id']}）, 会員: {member['name']}（ID: {record['member_id']}）, 延滞料金: {fine}円")

def list_available_books():
    available = [book for book in books if book["available_copies"] > 0]
    if not available:
        print("現在、貸出可能な図書はありません。")
        return
    print("--- 貸出可能な図書一覧 ---")
    for book in available:
        print(f"ID: {book['book_id']}, タイトル: {book['title']}, 著者: {book['author']}, 在庫: {book['available_copies']}")

def main():
    menu = [
        "1: 図書を追加",
        "2: 図書一覧を表示",
        "3: 図書を検索",
        "4: 会員を追加",
        "5: 会員一覧を表示",
        "6: 図書を貸し出す",
        "7: 貸出中の図書一覧を表示",
        "8: 図書を返却",
        "9: 延滞料金を計算",
        "10: 終了"
    ]
    while True:
        print("図書館管理システムメニュー:")
        for item in menu:
            print(item)
        try:
            choice = int(input("操作を選択してください（1-10）: "))
            if choice == 1:
                book_id = input("図書IDを入力してください: ")
                title = input("タイトルを入力してください: ")
                author = input("著者名を入力してください: ")
                copies = int(input("冊数を入力してください: "))
                add_book(book_id, title, author, copies)
            elif choice == 2:
                list_books()
            elif choice == 3:
                search_book()
            elif choice == 4:
                member_id = input("会員IDを入力してください: ")
                name = input("名前を入力してください: ")
                add_member(member_id, name)
            elif choice == 5:
                list_members()
            elif choice == 6:
                book_id = input("貸し出す図書IDを入力してください: ")
                member_id = input("会員IDを入力してください: ")
                borrow_book(book_id, member_id)
            elif choice == 7:
                list_borrowed_books()
            elif choice == 8:
                book_id = input("返却する図書IDを入力してください: ")
                member_id = input("会員IDを入力してください: ")
                return_book(book_id, member_id)
            elif choice == 9:
                calculate_fines()
            elif choice == 10:
                print("図書館管理システムを終了します。")
                break
            else:
                print("無効な選択です。1-10の数字を入力してください。")
        except ValueError as e:
            print(f"入力エラー: {e}")
        except Exception as e:
            print(f"予期しないエラーが発生しました: {e}")

if __name__ == "__main__":
    main()