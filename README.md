# Simple Todo - React Native Task Management App

A cross-platform mobile todo application built with React Native and Flask backend, featuring clean UI, task management, and real-time synchronization.

## 🚀 Features

- ✅ **Task Management**: Create, read, update, and delete tasks
- 📱 **Cross-Platform**: Works on both Android and iOS
- 🔄 **Real-time Sync**: Backend API integration with local storage fallback
- 🎨 **Clean UI**: Professional and intuitive user interface
- 📊 **Task Status**: Track pending and completed tasks
- 🗑️ **Swipe Actions**: Easy task completion and deletion
- 🔄 **Pull to Refresh**: Refresh tasks with pull-down gesture

## 📋 Prerequisites

Before you begin, ensure you have the following installed on your machine:

### For React Native Development:
- **Node.js** (v16 or higher) - [Download here](https://nodejs.org/)
- **npm** or **yarn** package manager
- **React Native CLI**: `npm install -g @react-native-community/cli`
- **Android Studio** (for Android development) - [Download here](https://developer.android.com/studio)
- **Xcode** (for iOS development, macOS only) - Available on Mac App Store

### For Backend Development:
- **Python** (v3.8 or higher) - [Download here](https://python.org/)
- **pip** package manager (comes with Python)

### Additional Tools:
- **Git** - [Download here](https://git-scm.com/)
- **Android Emulator** or physical Android device
- **iOS Simulator** (macOS only) or physical iOS device

## 🛠️ Installation & Setup

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd SimpleTodoApp
```

### 2. Backend Setup (Flask API)

Navigate to the backend directory:
```bash
cd TodoBackend
```

Create and activate virtual environment:
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:
```bash
pip install -r requirements.txt
```

Start the Flask server:
```bash
python src/main.py
```

The backend will run on `http://localhost:5000`

### 3. Frontend Setup (React Native)

Open a new terminal and navigate to the frontend directory:
```bash
cd SimpleTodo
```

Install dependencies:
```bash
npm install
# or
yarn install
```

### 4. Running the Mobile App

#### For Android:
1. Start Android emulator or connect Android device
2. Run the app:
```bash
npx react-native run-android
```

#### For iOS (macOS only):
1. Start iOS simulator or connect iOS device
2. Install iOS dependencies:
```bash
cd ios && pod install && cd ..
```
3. Run the app:
```bash
npx react-native run-ios
```

## 📱 Usage

1. **Adding Tasks**: Tap the input field at the top, enter your task, and press "Add"
2. **Completing Tasks**: Tap the circle next to a task to mark it as complete
3. **Deleting Tasks**: Tap the "Delete" button on any task
4. **Refreshing**: Pull down on the task list to refresh
5. **Viewing Status**: See pending and completed tasks in separate sections

## 🏗️ Architecture

```
SimpleTodoApp/
├── SimpleTodo/                 # React Native Frontend
│   ├── App.tsx                # Main app component
│   ├── android/               # Android-specific files
│   ├── ios/                   # iOS-specific files
│   └── package.json           # Frontend dependencies
│
├── TodoBackend/               # Flask Backend API
│   ├── src/
│   │   ├── models/
│   │   │   └── task.py       # Task database model
│   │   ├── routes/
│   │   │   └── task.py       # API endpoints
│   │   ├── database/
│   │   │   └── app.db        # SQLite database
│   │   └── main.py           # Flask app entry point
│   ├── venv/                 # Python virtual environment
│   └── requirements.txt      # Backend dependencies
│
└── README.md                 # This file
```

### Architecture Diagram

```
┌─────────────────┐    HTTP/REST API    ┌─────────────────┐
│                 │◄──────────────────►│                 │
│  React Native   │                    │   Flask API     │
│   Frontend      │                    │    Backend      │
│                 │                    │                 │
│  ┌───────────┐  │                    │  ┌───────────┐  │
│  │    UI     │  │                    │  │  Routes   │  │
│  │Components │  │                    │  │ /api/tasks│  │
│  └───────────┘  │                    │  └───────────┘  │
│  ┌───────────┐  │                    │  ┌───────────┐  │
│  │AsyncStorage│  │                    │  │  Models   │  │
│  │(Local DB) │  │                    │  │   Task    │  │
│  └───────────┘  │                    │  └───────────┘  │
└─────────────────┘                    │  ┌───────────┐  │
                                       │  │  SQLite   │  │
                                       │  │ Database  │  │
                                       │  └───────────┘  │
                                       └─────────────────┘
```

## 🔧 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/tasks` | Get all tasks |
| POST | `/api/tasks` | Create a new task |
| PUT | `/api/tasks/:id` | Update a task |
| DELETE | `/api/tasks/:id` | Delete a task |
| POST | `/api/tasks/:id/toggle` | Toggle task completion |

## 📝 Assumptions Made

1. **Simple Authentication**: No user authentication implemented for simplicity - all tasks are shared
2. **Local Storage**: App works offline using AsyncStorage, syncs when backend is available
3. **Basic Validation**: Minimal input validation (non-empty task titles)
4. **Single User**: Designed for single-user experience without user accounts
5. **Development Environment**: Configured for development with localhost backend
6. **Platform Support**: Focused on Android development, iOS support included but not extensively tested
7. **Database**: Using SQLite for simplicity instead of production databases
8. **Error Handling**: Basic error handling implemented, production apps would need more robust error management
9. **Styling**: Used native React Native components for cross-platform compatibility
10. **Dependencies**: Minimal dependencies to reduce complexity and potential conflicts

## 🎥 Demo Video

[📹 Watch Demo Video](https://www.loom.com/share/your-video-id)

*Note: Replace with actual Loom video link after recording*

## 🚨 Troubleshooting

### Common Issues:

1. **Metro bundler issues**: 
   ```bash
   npx react-native start --reset-cache
   ```

2. **Android build fails**:
   ```bash
   cd android && ./gradlew clean && cd ..
   npx react-native run-android
   ```

3. **iOS build fails**:
   ```bash
   cd ios && pod install && cd ..
   npx react-native run-ios
   ```

4. **Backend connection issues**:
   - Ensure Flask server is running on port 5000
   - Check if CORS is properly configured
   - Verify network connectivity

## 🔮 Future Enhancements

- [ ] User authentication and authorization
- [ ] Task categories and tags
- [ ] Due dates and reminders
- [ ] Task priority levels
- [ ] Search and filter functionality
- [ ] Dark mode support
- [ ] Push notifications
- [ ] Task sharing and collaboration
- [ ] Data export/import
- [ ] Advanced analytics

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📞 Support

If you encounter any issues or have questions, please:
1. Check the troubleshooting section above
2. Search existing issues in the repository
3. Create a new issue with detailed information

---

**This project is a part of a hackathon run by https://www.katomaran.com**

