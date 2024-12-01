css = '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #2b313e
}
.chat-message.bot {
    background-color: #475063
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #fff;
}
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://as1.ftcdn.net/v2/jpg/02/31/46/10/1000_F_231461036_iqWztZMUlDMcBn86HEJbct8hWtjAjeDI.jpg">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://img.freepik.com/free-vector/smiling-young-man-illustration_1308-174669.jpg?ga=GA1.1.305233641.1731152767&semt=ais_hybrid">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''
