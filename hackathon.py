class TutoringClass:
    def __init__(self, id, class_name, teacher_name, tuition_fee, student_count, operating_cost):
        self.id = id
        self.class_name = class_name
        self.teacher_name = teacher_name
        self.tuition_fee = tuition_fee
        self.student_count = student_count
        self.operating_cost = operating_cost
        self.total_revenue = 0.0
        self.revenue_type = ""
        self.update_financials()

    def calculate_revenue(self):
        self.total_revenue = (self.tuition_fee * self.student_count) - self.operating_cost

    def classify_revenue(self):
        if self.total_revenue < 0:
            self.revenue_type = "Lỗ"
        elif self.total_revenue < 10000000:
            self.revenue_type = "Thấp"
        elif self.total_revenue < 30000000:
            self.revenue_type = "Ổn định"
        else:
            self.revenue_type = "Tốt"

    def update_financials(self):
        self.calculate_revenue()
        self.classify_revenue()


class TutoringClassManager:
    def __init__(self):
        self.classes = []

    def is_id_exists(self, id):
        for c in self.classes:
            if c.id.strip().lower() == id.strip().lower():
                return True
        return False

    def add_class(self, tutoring_class):
        self.classes.append(tutoring_class)
        print("Thêm lớp học thành công!")

    def show_all(self):
        if not self.classes:
            print("Danh sách lớp học đang rỗng!")
            return

        print("\n" + "="*125)
        print(f"{'Mã lớp':<10} | {'Tên lớp học':<20} | {'Giáo viên':<20} | {'Học phí/HV':<12} | {'SL HV':<6} | {'CP Vận hành':<12} | {'Doanh thu':<15} | {'Phân loại'}")
        print("="*125)
        for c in self.classes:
            print(f"{c.id:<10} | {c.class_name:<20} | {c.teacher_name:<20} | {c.tuition_fee:<12,.0f} | {c.student_count:<6} | {c.operating_cost:<12,.0f} | {c.total_revenue:<15,.0f} | {c.revenue_type}")
        print("="*125)

    def update_class(self, id):
        for c in self.classes:
            if c.id.strip().lower() == id.strip().lower():
                print(f"\n--- Cập nhật thông tin lớp {c.id} ---")
                c.tuition_fee = get_valid_number("Nhập học phí mới: ", float, min_val=0)
                c.student_count = get_valid_number("Nhập số lượng học viên mới (0-100): ", int, min_val=0, max_val=100)
                c.operating_cost = get_valid_number("Nhập chi phí vận hành mới: ", float, min_val=0)
                c.update_financials()
                print("Cập nhật lớp học thành công!")
                return
        print("Không tìm thấy lớp học cần cập nhật!")

    def delete_class(self, id):
        for c in self.classes:
            if c.id.strip().lower() == id.strip().lower():
                confirm = input(f"Bạn có chắc muốn xóa lớp học '{c.id}' không? (Y/N): ").strip().lower()
                if confirm == 'y':
                    self.classes.remove(c)
                    print("\n[SUCCESS] Xóa lớp học thành công!")
                elif confirm == 'n':
                    print("\n[INFO] Đã hủy thao tác xóa.")
                else:
                    print("\n[ERROR] Lựa chọn không hợp lệ. Hủy thao tác xóa.")
                return
        print("\n[ERROR] Không tìm thấy lớp học cần xóa!")

    def search_class(self, keyword):
        keyword = keyword.strip().lower()
        results = [c for c in self.classes if keyword in c.class_name.lower() or keyword in c.teacher_name.lower()]

        if not results:
            print("\n[INFO] Không tìm thấy lớp học phù hợp!")
            return

        print(f"\n--- Kết quả tìm kiếm cho từ khóa '{keyword}' ---")
        print("="*125)
        print(f"{'Mã lớp':<10} | {'Tên lớp học':<20} | {'Giáo viên':<20} | {'Học phí/HV':<12} | {'SL HV':<6} | {'CP Vận hành':<12} | {'Doanh thu':<15} | {'Phân loại'}")
        print("="*125)
        for c in results:
            print(f"{c.id:<10} | {c.class_name:<20} | {c.teacher_name:<20} | {c.tuition_fee:<12,.0f} | {c.student_count:<6} | {c.operating_cost:<12,.0f} | {c.total_revenue:<15,.0f} | {c.revenue_type}")
        print("="*125)


def get_non_empty_string(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Trường này không được để trống! Vui lòng nhập lại.")

def get_valid_number(prompt, num_type, min_val=None, max_val=None):
    while True:
        try:
            val = num_type(input(prompt))
            if min_val is not None and val < min_val:
                print(f"Giá trị phải lớn hơn hoặc bằng {min_val}!")
                continue
            if max_val is not None and val > max_val:
                print(f"Giá trị tối đa được phép là {max_val}!")
                continue
            return val
        except ValueError:
            print(f"Sai kiểu dữ liệu! Vui lòng nhập số hợp lệ.")

def display_menu():
    print("\n================ MENU ================")
    print("1. Hiển thị danh sách lớp học")
    print("2. Thêm lớp học mới")
    print("3. Cập nhật lớp học")
    print("4. Xóa lớp học")
    print("5. Tìm kiếm lớp học")
    print("6. Thoát")
    print("=====================================")


def main():
    manager = TutoringClassManager()
    is_running = True

    while is_running:
        display_menu()
        choice = input("Nhập lựa chọn của bạn: ").strip()

        match choice:
            case '1':
                manager.show_all()
                
            case '2':
                print("\n--- THÊM LỚP HỌC MỚI ---")
                while True:
                    id_input = get_non_empty_string("Nhập mã lớp học: ")
                    if manager.is_id_exists(id_input):
                        print("[ERROR] Mã lớp học này đã tồn tại! Vui lòng nhập mã khác.")
                    else:
                        break
                
                class_name = get_non_empty_string("Nhập tên lớp học: ")
                teacher_name = get_non_empty_string("Nhập tên giáo viên: ")
                tuition_fee = get_valid_number("Nhập học phí mỗi học viên: ", float, min_val=0)
                student_count = get_valid_number("Nhập số lượng học viên (0-100): ", int, min_val=0, max_val=100)
                operating_cost = get_valid_number("Nhập chi phí vận hành lớp: ", float, min_val=0)

                new_class = TutoringClass(id_input, class_name, teacher_name, tuition_fee, student_count, operating_cost)
                manager.add_class(new_class)
                
            case '3':
                print("\n--- CẬP NHẬT LỚP HỌC ---")
                id_to_update = get_non_empty_string("Nhập mã lớp học cần cập nhật: ")
                manager.update_class(id_to_update)
                
            case '4':
                print("\n--- XÓA LỚP HỌC ---")
                id_to_delete = get_non_empty_string("Nhập mã lớp học cần xóa: ")
                manager.delete_class(id_to_delete)
                
            case '5':
                print("\n--- TÌM KIẾM LỚP HỌC ---")
                keyword = get_non_empty_string("Nhập tên lớp hoặc tên giáo viên cần tìm: ")
                manager.search_class(keyword)
                
            case '6':
                print("\nCảm ơn bạn đã sử dụng hệ thống quản lý lớp học thêm!")
                is_running = False
                
            case _:
                print("Lựa chọn không hợp lệ! Vui lòng chọn từ 1 đến 6.")

main()