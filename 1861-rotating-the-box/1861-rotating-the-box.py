class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        # 先順時針旋轉 90 度
        def rotate_matrix_90_clockwise(matrix):
            # 將矩陣的列轉置為行，並反轉每一列
            return [list(row[::-1]) for row in zip(*matrix)]
        
        # 讓石頭下落，處理重力
        def apply_gravity(matrix):
            rows = len(matrix)
            cols = len(matrix[0])
            for col in range(cols):
                empty_spot = rows - 1  # 從底部開始填充
                for row in range(rows - 1, -1, -1):
                    if matrix[row][col] == '#':  # 如果是石頭
                        matrix[row][col] = '.'  # 將石頭移動到空位
                        matrix[empty_spot][col] = '#'
                        empty_spot -= 1
                    elif matrix[row][col] == '*':  # 如果是障礙物
                        empty_spot = row - 1  # 更新空位為障礙物上方
            return matrix

        # 旋轉矩陣
        rotated_box = rotate_matrix_90_clockwise(box)
        # 處理重力，使石頭下落
        result = apply_gravity(rotated_box)
        return result