import json
import re

def main(arg1: str) -> dict:
    def process_input(input_str):
        result = []
        # 去掉字符串左右两边的方括号
        if input_str.startswith('[') and input_str.endswith(']'):
            input_str = input_str[1:-1]

        # 去掉所有换行符
        input_str = input_str.replace('\\n', '')
        input_str = input_str.replace('\\', '')
        input_str = input_str.replace('\'', '')
        input_str = input_str.replace('`', '')

        # 根据 "json" 字段进行切分
        json_fragments = re.split(r'json', input_str)

        for fragment in json_fragments:
            fragment = fragment.strip()
            if not fragment:
                continue

            if len(fragment) == 0:
                continue
            # 先判断是否包含 "无匹配的知识"，如果包含则跳过
            if "无匹配的知识" in fragment:
                continue

            try:
                if fragment.endswith(','):
                    fragment = fragment[0:-1]
                # 解析 JSON 数据
                data = json.loads(fragment)

                # 如果是 JSON 数组，将数组中的元素加入到结果集合中
                if isinstance(data, list):
                    result.extend(data)
                else:
                    result.append(data)

            except json.JSONDecodeError:
                # 如果 JSON 解析失败，跳过该项
                continue

        return result

    # 处理输入
    processed_data = process_input(arg1)

    # 将处理后的数据转换为 JSON 字符串
    jsonstr = json.dumps(processed_data, ensure_ascii=False)

    return {
        "result": jsonstr
    }

inputStr = "['```json\\n{\\n  \"结果\": \"无匹配的知识\"\\n}\\n```', '```json\\n[\\n    {\\n        \"问题场景\": \"质量类\",\\n        \"置信度\": 0.9,\\n        \"问题模块\": \"主材质量问题\",\\n        \"问题品类\": \"集成吊顶（厨房&卫生间）\",\\n        \"问题表现\": \"不牢固&异响&脱落\",\\n        \"问题空间\": \"未识别到\",\\n        \"问题原因\": \"安装质量问题\",\\n        \"推理过程\": \"结合客户描述的吊顶下沉与知识库中集成吊顶不牢固、异响和脱落的问题，判断为安装质量问题。\"\\n    },\\n    {\\n        \"问题场景\": \"质量类\",\\n        \"置信度\": 0.8,\\n        \"问题模块\": \"油漆施工质量问题\",\\n        \"问题品类\": \"墙面油漆施工\",\\n        \"问题表现\": \"开裂&磕碰&鼓包\",\\n        \"问题空间\": \"\",\\n        \"问题原因\": \"\",\\n        \"\",\\n\"推理过程\":\"结合客户描述的墙面油漆开裂与知识库中墙面油漆开裂、磕碰和鼓包的问题，判断为施工质量或其他原因。\"\\n}\\n]\\n```', '```json\\n[\\n    {\\n        \"问题场景\": \"质量类\",\\n        \"置信度\": 0.9,\\n        \"问题模块\": \"油漆施工质量问题\",\\n        \"问题品类\": \"墙面油漆施工\",\\n        \"问题表现\": \"开裂&磕碰&鼓包\",\\n        \"问题空间\": \"未提及具体空间\",\\n        \"问题原因\": \"施工质量问题\",\\n        \"推理过程\": \"结合知识和输入得出结果的推理过程\"\\n    }\\n]\\n```', '```json\\n[\\n    {\\n        \"问题场景\": \"质量类\",\\n        \"置信度\": 0.9,\\n        \"问题模块\": \"油漆施工质量问题\",\\n        \"问题品类\": \"墙面油漆施工\",\\n        \"问题表现\": \"开裂&磕碰&鼓包\",\\n        \"问题空间\": \"未提及具体空间\",\\n        \"问题原因\": \"施工质量问题\",\\n        \"推理过程\": \"结合客户描述的\\'新旧墙体交界处油漆开裂\\'，以及知识库中关于墙面油漆施工出现开裂的描述，判断为施工质量问题。\"\\n    }\\n]\\n```', '```json\\n{\\n  \"问题场景\": \"质量类\",\\n  \"置信度\": 0.7,\\n  \"问题模块\": \"主材质量问题\",\\n  \"问题品类\": \"其他软装材料\",\\n  \"问题表现\": \"表面划痕&缺陷&脏污&磕碰\",\\n  \"问题空间\": \"\",\\n  \"问题原因\": \"材料质量问题\",\\n  \"推理过程\": \"阴角开裂可能是由于使用的其他软装材料本身的质量不佳，导致在施工或使用过程中出现裂缝。结合知识库中关于其他软装材料表面易出现划痕、缺陷和脏污的描述，推断出此类问题可能与材料质量有关。\"\\n}\\n```']"

result= main(inputStr)

print(result)