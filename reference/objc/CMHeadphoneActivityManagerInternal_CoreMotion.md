# `CMHeadphoneActivityManagerInternal`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 26 instance variables, 0 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _dispatchQueue;
@"RMConnectionClient" _activityConnectionClient;
@"NSOperationQueue" _activityCallbackQueue;
@? _activityHandler;
B _activityActive;
B _activityStreaming;
@"RMConnectionClient" _statusConnectionClient;
@"NSOperationQueue" _statusCallbackQueue;
@? _statusHandler;
B _statusActive;
B _statusStreaming;
B _deviceConnected;
d _startTime;
{unique_ptr<CLSettings, std::default_delete<CLSettings>>=""{?="__ptr_"^{CLSettings}}} _motionSettings;
B _enableMSL;
f _accessoryAccelInterval;
f _accessoryGyroInterval;
B _isGyroBiasValid;
f _accessoryDeviceMotionInterval;
f _sourceDeviceMotionInterval;
{unique_ptr<CLMotionNotifier::Dispatcher, std::default_delete<CLMotionNotifier::Dispatcher>>=""{?="__ptr_"^{Dispatcher}}} _accessoryAccelerometerDispatcher;
{unique_ptr<CLMotionNotifier::Dispatcher, std::default_delete<CLMotionNotifier::Dispatcher>>=""{?="__ptr_"^{Dispatcher}}} _accessoryGyroDispatcher;
{unique_ptr<CLMotionNotifier::Dispatcher, std::default_delete<CLMotionNotifier::Dispatcher>>=""{?="__ptr_"^{Dispatcher}}} _accessoryDeviceMotionDispatcher;
{unique_ptr<CLMotionNotifier::Dispatcher, std::default_delete<CLMotionNotifier::Dispatcher>>=""{?="__ptr_"^{Dispatcher}}} _accessoryDeviceMotionConfigDispatcher;
{unique_ptr<CLMotionNotifier::Dispatcher, std::default_delete<CLMotionNotifier::Dispatcher>>=""{?="__ptr_"^{Dispatcher}}} _deviceMotionDispatcher;
{unique_ptr<CMSpatialLogger, std::default_delete<CMSpatialLogger>>=""{?="__ptr_"^{CMSpatialLogger}}} fLogger;
```

## Instance methods

```
-[CMHeadphoneActivityManagerInternal init];
-[CMHeadphoneActivityManagerInternal dealloc];
-[CMHeadphoneActivityManagerInternal updatePreferences];
-[CMHeadphoneActivityManagerInternal connectActivity];
-[CMHeadphoneActivityManagerInternal connectStatus];
-[CMHeadphoneActivityManagerInternal disconnectActivity];
-[CMHeadphoneActivityManagerInternal disconnectStatus];
-[CMHeadphoneActivityManagerInternal mslLoggingEnabledPrivate];
-[CMHeadphoneActivityManagerInternal onAudioAccessoryDeviceMotion:];
-[CMHeadphoneActivityManagerInternal startMslLoggingPrivateWithFilenamePrefix:filePath:];
-[CMHeadphoneActivityManagerInternal stopMslLoggingPrivate];
```
