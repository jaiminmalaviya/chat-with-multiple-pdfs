css = """
<style>
.chat-message {
    padding: 1rem; 
    border-radius: 0.5rem; 
    margin-bottom: 1rem; 
    display: flex
}
.chat-message.user {
    background-color: #2b313e
}
.chat-message.bot {
    background-color: #475063
}
.chat-message .avatar {
  width: 10%;
}
.chat-message .avatar img {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 90%;
  padding: 0 1rem;
  color: #fff;
  display: flex;
  align-items: center;
}
"""

bot_template = """
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://img.freepik.com/premium-photo/ai-robot-head-design_767081-269.jpg" style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: cover;">
    </div>
    <div class="message">{{MSG}}</div>
</div>
"""

user_template = """
<div class="chat-message user">
    <div class="avatar">
        <img src="https://cdn3.iconfinder.com/data/icons/business-avatar-1/512/10_avatar-512.png">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
"""
