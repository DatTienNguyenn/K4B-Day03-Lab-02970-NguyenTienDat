"""
🛠️ TOOL DEFINITIONS & EXECUTION BACKEND
Mã nguồn chứa danh sách Tool Schemas (JSON Schema) và Execution Layer phục vụ cho MCP Server.
"""

import json
from typing import Dict, Any

# ==============================================================================
# 1. KHAI BÁO TOOL SCHEMAS CHUẨN NATIVE JSON SCHEMA (TASK 1.2)
# ==============================================================================

TOOLS_SCHEMA = [
    # Tool 1: Đã được định nghĩa mẫu sẵn cho Học viên tham khảo
    # {
    #     "name": "academic_query",
    #     "description": "Tra cứu hồ sơ và thông tin học vụ của sinh viên VinUni bằng mã sinh viên.",
    #     "parameters": {
    #         "type": "object",
    #         "properties": {
    #             "student_id": {
    #                 "type": "string",
    #                 "description": "Mã sinh viên cần tra cứu (ví dụ: 'SV2026001')"
    #             }
    #         },
    #         "required": ["student_id"]
    #     }
    # },
    
    # --------------------------------------------------------------------------
    # TODO 1.2: HỌC VIÊN HOÀN THIỆN TOOL SCHEMA CHO 'schedule_appointment'
    # 🎯 YÊU CẦU THIẾT KẾ SCHEMA (JSON SCHEMA STANDARD):
    # 1. Tool dùng để đặt lịch hẹn tư vấn học vụ với Cố vấn học tập VinUni.
    # 2. Thiết kế các tham số (properties) để LLM trích xuất:
    #    - student_id (string): Mã sinh viên cần đặt lịch (ví dụ: 'SV2026001')
    #    - datetime_str (string): Thời gian hẹn (ví dụ: '14:00 15/09/2026')
    #    - advisor_name (string): Tên cố vấn học tập
    # 3. Khai báo danh sách các trường bắt buộc (required).
    # --------------------------------------------------------------------------
    {
        "name": "check_room_availability",
        "description": "Kiểm tra tình trạng sẵn sàng của phòng họp.",
        "parameters": {
            "type": "object",
            "properties": {
                "room_id": {
                    "type": "string",
                    "description": "Mã phòng cần kiểm tra (ví dụ: 'P302')"
                },
                "start_time": {
                    "type": "string",
                    "description": "Thời gian bắt đầu (ví dụ: '14:00')"
                },
                "end_time": {
                    "type": "string",
                    "description": "Thời gian kết thúc (ví dụ: '16:00')"
                },
                "date": {
                    "type": "string",
                    "description": "Ngày cần kiểm tra (ví dụ: 'hôm nay')"
                }
            },
            "required": [
                "room_id",
                "start_time",
                "end_time",
                "date"
            ] 
        }
    },
    {
        "name": "book_room_and_equipment",
        "description": "Đặt phòng họp và thiết bị kèm theo.",
        "parameters": {
            "type": "object",
            "properties": {
                "room_id": {
                    "type": "string",
                    "description": "Mã phòng cần đặt (ví dụ: 'A101')"
                },
                "equipments": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "type": {
                                "type": "string",
                                "description": "Loại thiết bị (ví dụ: 'wireless_mic')"
                            },
                            "quantity": {
                                "type": "integer",
                                "description": "Số lượng thiết bị"
                            }
                        },
                        "required": ["type", "quantity"]
                    }
                },
                "start_time": {
                    "type": "string",
                    "description": "Thời gian bắt đầu (ví dụ: '09:00')"
                },
                "end_time": {
                    "type": "string",
                    "description": "Thời gian kết thúc (ví dụ: '11:00')"
                },
                "capacity": {
                    "type": "integer",
                    "description": "Sức chứa của phòng họp"
                }
            },
            "required": [
                "room_id",
                "equipments",
                "start_time",
                "end_time",
                "capacity"
            ]
        }
    },
    {
        "name": "find_available_rooms",
        "description": "Tìm các phòng họp còn trống trong khoảng thời gian nhất định.",
        "parameters": {
            "type": "object",
            "properties": {
                "start_time": {
                    "type": "string",
                    "description": "Thời gian bắt đầu (ví dụ: '09:00')"
                },
                "end_time": {
                    "type": "string",
                    "description": "Thời gian kết thúc (ví dụ: '11:00')"
                },
                "date": {
                    "type": "string",
                    "description": "Ngày cần kiểm tra (ví dụ: 'hôm nay')"
                },
                "capacity": {
                    "type": "integer",
                    "description": "Sức chứa tối thiểu của phòng họp"
                }
            },
            "required": [            ]
        }
    },
    {
        "name": "check_equipment_availability",
        "description": "Kiểm tra tình trạng sẵn sàng của thiết bị.",
        "parameters": {
            "type": "object",
            "properties": {
                "equipment_type": {
                    "type": "string",
                    "description": "Loại thiết bị cần kiểm tra (ví dụ: 'wireless_mic')"
                },
                "quantity": {
                    "type": "integer",
                    "description": "Số lượng thiết bị cần kiểm tra"
                },
                "date": {
                    "type": "string",
                    "description": "Ngày cần kiểm tra (ví dụ: 'hôm nay')"
                }
            },
            "required": [
                "equipment_type",
                "quantity",
                "date"
            ]
        }
    },
    {
        "name": "find_available_equipment",
        "description": "Tìm các thiết bị còn trống trong khoảng thời gian nhất định.",
        "parameters": {
            "type": "object",
            "properties": {
                "start_time": {
                    "type": "string",
                    "description": "Thời gian bắt đầu (ví dụ: '09:00')"
                },
                "end_time": {
                    "type": "string",
                    "description": "Thời gian kết thúc (ví dụ: '11:00')"
                },
                "date": {
                    "type": "string",
                    "description": "Ngày cần kiểm tra (ví dụ: 'hôm nay')"
                }
            },
            "required": [
            ]
        }
    }
]

# ==============================================================================
# 2. MÔ PHỎNG DỮ LIỆU & HÀM THỰC THI TOOL (EXECUTION LAYER)
# ==============================================================================

# MOCK_DATABASE = {
#     "SV2026001": {
#         "full_name": "Nguyễn Văn An",
#         "class": "AI-K4",
#         "gpa": 3.85,
#         "email": "an.nv@vinuni.edu.vn",
#         "status": "Đang học",
#         "advisor": "PGS.TS Nguyễn Văn A"
#     },
#     "SV2026002": {
#         "full_name": "Trần Thị Bình",
#         "class": "AI-K4",
#         "gpa": 3.60,
#         "email": "binh.tt@vinuni.edu.vn",
#         "status": "Đang học",
#         "advisor": "TS. Lê Thị B"
#     }
# }


# def execute_academic_query(student_id: str) -> str:
#     """Thực thi tra cứu học vụ theo mã sinh viên"""
#     student = MOCK_DATABASE.get(student_id.strip().upper())
#     if student:
#         return json.dumps({
#             "status": "SUCCESS",
#             "student_id": student_id,
#             "data": student
#         }, ensure_ascii=False)
#     else:
#         return json.dumps({
#             "status": "NOT_FOUND",
#             "message": f"Không tìm thấy dữ liệu sinh viên có mã '{student_id}'"
#         }, ensure_ascii=False)


# def execute_schedule_appointment(student_id: str, datetime_str: str, advisor_name: str = "PGS.TS Nguyễn Văn A") -> str:
#     """Thực thi đặt lịch hẹn tư vấn học vụ"""
#     return json.dumps({
#         "status": "SUCCESS",
#         "booking_id": f"BK-{student_id}-99",
#         "student_id": student_id,
#         "datetime": datetime_str,
#         "advisor": advisor_name,
#         "message": f"Đặt lịch thành công cho sinh viên {student_id} với {advisor_name} vào lúc {datetime_str}."
#     }, ensure_ascii=False)

def check_room_availability(room_id: str, start_time: str, end_time: str, date: str) -> str:
    """Thực thi kiểm tra tình trạng sẵn sàng của phòng họp"""
    # Giả lập logic kiểm tra phòng họp
    available = True  # Giả sử phòng luôn sẵn sàng
    return json.dumps({
        "status": "SUCCESS",
        "room_id": room_id,
        "available": available,
        "start_time": start_time,
        "end_time": end_time,
        "date": date,
        "message": f"Phòng {room_id} {'còn trống' if available else 'không còn trống'} từ {start_time} đến {end_time} vào ngày {date}."
    }, ensure_ascii=False)

def check_equipment_availability(equipment_type: str, quantity: int, date: str) -> str:
    """Thực thi kiểm tra tình trạng sẵn sàng của thiết bị"""
    # Giả lập logic kiểm tra thiết bị
    available_quantity = 10  # Giả sử luôn có 10 thiết bị sẵn sàng
    is_available = available_quantity >= quantity
    return json.dumps({
        "status": "SUCCESS",
        "equipment_type": equipment_type,
        "requested_quantity": quantity,
        "available_quantity": available_quantity,
        "is_available": is_available,
        "date": date,
        "message": f"Thiết bị {equipment_type} {'còn sẵn sàng' if is_available else 'không còn sẵn sàng'} với số lượng {quantity} vào ngày {date}."
    }, ensure_ascii=False)

def find_available_rooms(start_time: str, end_time: str, date: str, capacity: int) -> str:
    """Thực thi tìm các phòng họp còn trống"""
    # Giả lập logic tìm phòng họp
    available_rooms = ["A101", "B202", "C303"]  # Giả sử có 3 phòng sẵn sàng
    return json.dumps({
        "status": "SUCCESS",
        "available_rooms": available_rooms,
        "start_time": start_time,
        "end_time": end_time,
        "date": date,
        "capacity": capacity,
        "message": f"Tìm thấy {len(available_rooms)} phòng họp còn trống từ {start_time} đến {end_time} vào ngày {date} với sức chứa >= {capacity} bao gồm các phòng: {', '.join(available_rooms)}."
    }, ensure_ascii=False)

def find_available_equipment(start_time: str, end_time: str, date: str) -> str:
    """Thực thi tìm các thiết bị còn trống"""
    # Giả lập logic tìm thiết bị
    available_equipments = [
        {"type": "wireless_mic", "quantity": 5},
        {"type": "projector", "quantity": 2}
    ]  # Giả sử có 5 micro không dây và 2 máy chiếu sẵn sàng
    return json.dumps({
        "status": "SUCCESS",
        "available_equipments": available_equipments,
        "start_time": start_time,
        "end_time": end_time,
        "date": date,
        "message": f"Tìm thấy {len(available_equipments)} thiết bị còn trống từ {start_time} đến {end_time} vào ngày {date}."
    }, ensure_ascii=False)

def book_room_and_equipment(room_id: str, equipments: list, start_time: str, end_time: str, capacity: int) -> str:
    """Thực thi đặt phòng họp và thiết bị kèm theo"""
    # Giả lập logic đặt phòng và thiết bị
    booking_id = f"BK-{room_id}-{start_time.replace(':', '')}"
    return json.dumps({
        "status": "SUCCESS",
        "booking_id": booking_id,
        "room_id": room_id,
        "equipments": equipments,
        "start_time": start_time,
        "end_time": end_time,
        "capacity": capacity,
        "message": f"Đặt phòng {room_id} và thiết bị thành công từ {start_time} đến {end_time}."
    }, ensure_ascii=False)

# Router gọi tool thực tế
TOOL_ROUTER = {
    "check_room_availability": check_room_availability,
    "check_equipment_availability": check_equipment_availability,
    "find_available_rooms": find_available_rooms,
    "find_available_equipment": find_available_equipment,
    "book_room_and_equipment": book_room_and_equipment
}

def dispatch_tool_call(tool_name: str, arguments: Dict[str, Any]) -> str:
    """Hàm trung chuyển thực thi tool"""
    if tool_name in TOOL_ROUTER:
        try:
            return TOOL_ROUTER[tool_name](**arguments)
        except Exception as e:
            return json.dumps({"status": "EXECUTION_ERROR", "error": str(e)}, ensure_ascii=False)
    return json.dumps({"status": "UNKNOWN_TOOL", "error": f"Tool '{tool_name}' không tồn tại!"}, ensure_ascii=False)
