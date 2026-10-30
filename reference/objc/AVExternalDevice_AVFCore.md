# `AVExternalDevice`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 27 properties, 46 instance methods, 3 class methods

## Instance variables

```
@"AVExternalDeviceInternal" _externalDevice;
```

## Properties

```
@property (T@"<AVExternalDeviceDelegate>",N) delegate;
@property (T@"NSArray",R,N) screenIDs;
@property (T@"NSDictionary",R,N) screenInputCapabilities;
@property (T@"NSDictionary",R,N) screenPrimaryInputDevices;
@property (T@"NSDictionary",R,N) screenViewAreas;
@property (T@"NSDictionary",R,N) screenSafeAreas;
@property (T@"NSData",R,N) OEMIcon;
@property (T@"NSArray",R,N) OEMIcons;
@property (T@"NSString",R,N) OEMIconLabel;
@property (TB,R,N) OEMIconVisible;
@property (T@"NSString",R,N) modelName;
@property (T@"NSArray",R,N) externalDeviceHIDs;
@property (TB,R,N) nightMode;
@property (TB,R,N) nightModeSupported;
@property (TB,R,N) rightHandDrive;
@property (T@"NSArray",R,N) limitedUIElements;
@property (TB,R,N) limitedUI;
@property (TB,R,N) ownsScreen;
@property (TB,R,N) ownsTurnByTurnNavigation;
@property (TB,R,N) recognizingSpeech;
@property (T@"NSArray",R,N) supportedFeatures;
@property (Tq,R,N) electronicTollCollection;
@property (Tq,R,N) navigationAidedDriving;
@property (T@"NSString",R,N) name;
@property (T@"NSString",R,N) ID;
@property (Tq,R,N) transportType;
@property (T@"NSData",R,N) MFiCertificateSerialNumber;
```

## Class methods

```
+[AVExternalDevice sharedLocalDevice];
+[AVExternalDevice currentCarPlayExternalDevice];
+[AVExternalDevice currentExternalDevice];
```

## Instance methods

```
-[AVExternalDevice nightMode];
-[AVExternalDevice rightHandDrive];
-[AVExternalDevice ID];
-[AVExternalDevice recognizingSpeech];
-[AVExternalDevice supportedFeatures];
-[AVExternalDevice requestTurnByTurnNavigationOwnership];
-[AVExternalDevice electronicTollCollection];
-[AVExternalDevice init];
-[AVExternalDevice OEMIcons];
-[AVExternalDevice takeScreenForClient:reason:];
-[AVExternalDevice dealloc];
-[AVExternalDevice transportType];
-[AVExternalDevice ownsTurnByTurnNavigation];
-[AVExternalDevice requestCarUIForURL:withUUID:];
-[AVExternalDevice requestViewArea:forScreenID:];
-[AVExternalDevice OEMIconLabel];
-[AVExternalDevice setDelegate:];
-[AVExternalDevice _weakReference];
-[AVExternalDevice OEMIconVisible];
-[AVExternalDevice delegate];
-[AVExternalDevice nightModeSupported];
-[AVExternalDevice limitedUIElements];
-[AVExternalDevice navigationAidedDriving];
-[AVExternalDevice limitedUI];
-[AVExternalDevice borrowScreenForClient:reason:];
-[AVExternalDevice MFiCertificateSerialNumber];
-[AVExternalDevice name];
-[AVExternalDevice modelName];
-[AVExternalDevice screenIDs];
-[AVExternalDevice OEMIcon];
-[AVExternalDevice screenSafeAreas];
-[AVExternalDevice screenViewAreas];
-[AVExternalDevice _figEndpointPropertyValueForKey:];
-[AVExternalDevice _screenInfo];
-[AVExternalDevice _triggerFakeNotificationNamed:withPayload:];
-[AVExternalDevice externalDeviceHIDWithUUID:];
-[AVExternalDevice externalDeviceHIDs];
-[AVExternalDevice figEndpoint];
-[AVExternalDevice initWithFigEndpoint:];
-[AVExternalDevice ownsScreen];
-[AVExternalDevice requestCarUI];
-[AVExternalDevice requestCarUIForURL:];
-[AVExternalDevice screenInputCapabilities];
-[AVExternalDevice screenPrimaryInputDevices];
-[AVExternalDevice sendCommand:withParameters:];
-[AVExternalDevice takeScreenForConnection];
```
