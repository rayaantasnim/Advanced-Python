class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, task):
        self.items.append(task)
        print(f"✅ Task '{task}' added to queue!")

    def dequeue(self):
        if not self.isEmpty():
            task = self.items.pop(0)
            print(f"⚡ Task '{task}' executed and removed!")
            return task
        else:
            print("❌ Queue is empty! Nothing to execute.")
            return None

    def front(self):
        if not self.isEmpty():
            return self.items[0]
        return None

    def rear(self):
        if not self.isEmpty():
            return self.items[-1]
        return None

    def isEmpty(self):
        return len(self.items) == 0

    def display(self):
        if self.isEmpty():
            print("📭 Queue is empty.")
        else:
            print("📋 Current Queue:")
            i = 1
            for task in self.items:
                print(f"{i}. {task}")
                i += 1

    def clearAll(self):
        confirm = input("⚠️ Are you sure you want to clear all tasks? (Y/N): ")
        if confirm.lower() == "y":
            self.items.clear()
            print("🗑️ All tasks removed! Queue is now empty.")
        else:
            print("❎ Clear cancelled.")


# 🎮 Interactive Simulator
scheduler = Queue()

while True:
    print("\n---  🕹️   Task Scheduler Menu ---")
    print("1️⃣    Add Task (enqueue)")
    print("2️⃣    Execute Task (dequeue)")
    print("3️⃣    See Next Task (front)")
    print("4️⃣    See Last Task (rear)")
    print("5️⃣    Show All Tasks")
    print("6️⃣    Remove All Tasks 🗑️")
    print("7️⃣    Exit 🚪")

    choice = input("👉 Enter choice (1-7): ")

    if choice == "1":
        task = input("✍️ Enter task name: ")
        scheduler.enqueue(task)

    elif choice == "2":
        scheduler.dequeue()

    elif choice == "3":
        task = scheduler.front()
        if task:
            print(f"👀 Next task: {task}")
        else:
            print("📭 Queue is empty.")

    elif choice == "4":
        task = scheduler.rear()
        if task:
            print(f"🔚 Last task: {task}")
        else:
            print("📭 Queue is empty.")

    elif choice == "5":
        scheduler.display()

    elif choice == "6":
        scheduler.clearAll()

    elif choice == "7":
        print("👋 Exiting Task Scheduler. Bye bye!")
        break

    else:
        print("⚠️ Invalid choice! Please try again.")