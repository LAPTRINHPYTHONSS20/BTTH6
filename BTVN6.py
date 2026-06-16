import logging

# Cấu hình logging
logging.basicConfig(
    filename='arena_tickets.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Mock Data
tickets = [
    {"ticket_id": "T01", "buyer_name": "Nguyen Van A", "price": 500.0, "status": "Booked", "seat": ("A", 1)},
    {"ticket_id": "T02", "buyer_name": "Tran Thi B", "price": 300.0, "status": "Cancelled", "seat": ("B", 5)},
    {"ticket_id": "T03", "buyer_name": "Le Van C", "price": 500.0, "status": "Booked", "seat": ("A", 2)}
]

def display_tickets(tickets):
    print("\n--- DANH SÁCH VÉ ---")
    if not tickets:
        print("Hiện chưa có vé nào trong hệ thống.")
        return
    print(f"{'Mã Vé':<8} | {'Tên Khách Hàng':<15} | {'Giá Vé':<8} | {'Chỗ Ngồi':<8} | {'Trạng Thái'}")
    print("-" * 60)
    for t in tickets:
        try:
            status_display = t['status']
            if t['status'] == "Cancelled": status_display += " [ĐÃ HỦY]"
            seat_str = f"{t['seat'][0]}-{t['seat'][1]}"
            print(f"{t['ticket_id']:<8} | {t['buyer_name']:<15} | {t['price']:<8} | {seat_str:<8} | {status_display}")
        except KeyError as e:
            print("Lỗi: Một vé đang bị thiếu dữ liệu, vui lòng kiểm tra lại.")
            logging.error(f"Missing key while displaying ticket: {e}")
            break
    logging.info("User viewed ticket list.")

def book_ticket(tickets):
    print("\n--- ĐẶT VÉ MỚI ---")
    tid = input("Nhập mã vé: ")
    if any(t['ticket_id'] == tid for t in tickets):
        print(f"Lỗi: Mã vé {tid} đã tồn tại.")
        logging.warning(f"Duplicate ticket ID entered: {tid}")
        return
    
    name = input("Nhập tên khách hàng: ")
    while True:
        try:
            price = float(input("Nhập giá vé: "))
            if price <= 0: raise ValueError
            break
        except ValueError:
            print("Giá vé phải là số lớn hơn 0.")
    
    row = input("Nhập khu vực ghế: ").upper()
    while True:
        try:
            num = int(input("Nhập số ghế: "))
            break
        except ValueError:
            print("Số ghế phải là số nguyên.")
            
    tickets.append({"ticket_id": tid, "buyer_name": name, "price": price, "status": "Booked", "seat": (row, num)})
    logging.info(f"Booked new ticket {tid} for {name}")

def calculate_revenue(tickets):
    print("\n--- BÁO CÁO DOANH THU ---")
    total = 0.0
    booked_count = 0
    cancelled_count = 0
    try:
        for t in tickets:
            if t['status'] == "Booked":
                total += t['price']
                booked_count += 1
            else:
                cancelled_count += 1
        print(f"Tổng số vé đã đặt: {booked_count}")
        print(f"Tổng số vé đã hủy: {cancelled_count}")
        print(f"Tổng doanh thu hợp lệ: {total:.1f}")
        logging.info(f"Revenue report generated. Total: {total}")
    except KeyError as e:
        print("Lỗi: Một vé đang bị thiếu dữ liệu doanh thu.")
        logging.error(f"Missing key while calculating revenue: {e}")

# ... (Bạn bổ sung hàm change_seat và cancel_ticket tương tự logic trên)

def main():
    while True:
        print("\n=== HỆ THỐNG QUẢN LÝ VÉ RIKKEI ESPORTS ===")
        print("1. Xem vé | 2. Đặt vé | 3. Đổi chỗ | 4. Hủy vé | 5. Báo cáo | 6. Thoát")
        choice = input("Chọn chức năng: ")
        if choice == '1': display_tickets(tickets)
        elif choice == '2': book_ticket(tickets)
        elif choice == '5': calculate_revenue(tickets)
        elif choice == '6':
            logging.info("Ticket management system closed.")
            break

if __name__ == "__main__":
    main()
