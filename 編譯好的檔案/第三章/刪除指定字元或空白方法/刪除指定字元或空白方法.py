print("  spacious  ".strip()) # str.strip 從字串兩側刪除選擇性參數所指定的字元，一旦碰到不是指定的字元就停止刪除，並傳回剩下的字串，選擇性參數可以不寫，表示指定的字元為空白，即刪除字串兩側的空白
# 刪除字串兩側的空白
print("www.example.com".strip("comwz."))
#刪除字串兩側的comwz.字元

print("  spacious  ".lstrip()) # str.lstrip 從字串左側刪除選擇性參數所指定的字元，一旦碰到不是指定的字元就停止刪除，並傳回剩下的字串，選擇性參數可以不寫，表示指定的字元為空白，即刪除字串兩側的空白
# 刪除字串左側的空白
print("www.example.com".lstrip("comwz."))
#刪除字串左側的comwz.字元

print("  spacious  ".rstrip()) # str.rstrip 從字串右側刪除選擇性參數所指定的字元，一旦碰到不是指定的字元就停止刪除，並傳回剩下的字串，選擇性參數可以不寫，表示指定的字元為空白，即刪除字串兩側的空白
# 刪除字串右側的空白
print("www.example.com".rstrip("comwz."))
#刪除字串右側的comwz.字元
