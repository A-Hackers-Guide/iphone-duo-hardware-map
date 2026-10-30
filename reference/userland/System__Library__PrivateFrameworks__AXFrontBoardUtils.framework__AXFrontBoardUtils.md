# `/System/Library/PrivateFrameworks/AXFrontBoardUtils.framework/AXFrontBoardUtils`

iOS 27.2 dyld shared cache image. Version `3245.8.9.0.0`. **[DSC]**

## Linked libraries (20)

- `/System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices`
- `/System/Library/Frameworks/CoreHaptics.framework/CoreHaptics`
- `/usr/lib/libAccessibility.dylib`
- `/System/Library/Frameworks/CoreServices.framework/CoreServices`
- `/System/Library/PrivateFrameworks/AXGuestPassServices.framework/AXGuestPassServices`
- `/System/Library/PrivateFrameworks/NanoPreferencesSync.framework/NanoPreferencesSync`
- `/System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard`
- `/System/Library/PrivateFrameworks/AXRuntime.framework/AXRuntime`
- `/System/Library/Frameworks/CoreGraphics.framework/CoreGraphics`
- `/System/Library/Frameworks/UIKit.framework/UIKit`
- `/System/Library/PrivateFrameworks/PairedDeviceRegistry.framework/PairedDeviceRegistry`
- `/System/Library/Frameworks/Foundation.framework/Foundation`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`
- `/System/Library/PrivateFrameworks/AccessibilityUtilities.framework/AccessibilityUtilities`
- `/System/Library/PrivateFrameworks/AXIDSServices.framework/AXIDSServices`
- `/System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard`
- `/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`
- `/System/Library/PrivateFrameworks/AudioSession.framework/AudioSession`
- `/usr/lib/libobjc.A.dylib`
- `/usr/lib/libSystem.B.dylib`

## Objective-C: 8 classes, 5 protocols, 103 methods, 56 properties

### Class pages

Every class and protocol, with its methods: [`AXFBFakeProcess`](../objc/AXFBFakeProcess_AXFrontBoardUtils.md), [`AXFBFakeProcessState`](../objc/AXFBFakeProcessState_AXFrontBoardUtils.md), [`AXFrontBoardProcessWatcher`](../objc/AXFrontBoardProcessWatcher_AXFrontBoardUtils.md), [`AXIDSServicesClient`](../objc/AXIDSServicesClient_AXFrontBoardUtils.protocol.md), [`AXIOSAutoAnswerHelper`](../objc/AXIOSAutoAnswerHelper_AXFrontBoardUtils.md), [`AXServerInstanceActionHandlerHelper`](../objc/AXServerInstanceActionHandlerHelper_AXFrontBoardUtils.md), [`FBProcessManagerObserver`](../objc/FBProcessManagerObserver_AXFrontBoardUtils.protocol.md), [`FBProcessObserver`](../objc/FBProcessObserver_AXFrontBoardUtils.protocol.md), [`NSObject`](../objc/NSObject_AXFrontBoardUtils.protocol.md), [`UIApplicationSceneSettings`](../objc/UIApplicationSceneSettings_AXFrontBoardUtils.protocol.md)

### Classes

`AXFBFakeProcess`, `AXFBFakeProcessState`, `AXFrontBoardProcessWatcher`, `AXIOSAutoAnswerHelper`, `AXServerInstanceActionHandlerHelper`, `FBSScene`, `FBScene`, `UIApplication`

### Protocols

`AXIDSServicesClient`, `FBProcessManagerObserver`, `FBProcessObserver`, `NSObject`, `UIApplicationSceneSettings`

### Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSString",R,N) persistenceIdentifier;
@property (TB,R,N) underLock;
@property (TQ,R,N) statusBarStyleOverridesToSuppress;
@property (TQ,R,N) deactivationReasons;
@property (Tq,R,N) userInterfaceStyle;
@property (T@"NSNumber",R,N) forcedStatusBarStyle;
@property (TB,R,N) forcedStatusBarForegroundTransparent;
@property (TB,R,N) deviceOrientationEventsEnabled;
@property (TB,R,N) canShowAlerts;
@property (TB,R,N) idleModeEnabled;
@property (TB,R,N) statusBarDisabled;
@property (T{UIEdgeInsets=dddd},R,N) peripheryInsets;
@property (Tq,R,N) statusBarParts;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) statusBarAvoidanceFrame;
@property (Td,R,N) statusBarHeight;
@property (Td,R,N) systemMinimumMargin;
@property (T{UIEdgeInsets=dddd},R,N) safeAreaInsetsPortrait;
@property (Td,R,N) homeAffordanceOverlayAllowance;
@property (T{UIEdgeInsets=dddd},R,N) safeAreaInsetsLandscapeLeft;
@property (T{UIEdgeInsets=dddd},R,N) safeAreaInsetsPortraitUpsideDown;
@property (T{UIEdgeInsets=dddd},R,N) safeAreaInsetsLandscapeRight;
@property (Tq,R,N) deviceOrientation;
@property (TQ,R,N) artworkSubtype;
@property (T@"BSCornerRadiusConfiguration",R,N) cornerRadiusConfiguration;
@property (TI,R,N) hostContextIdentifierForSnapshotting;
@property (TQ,R,N) scenePresenterRenderIdentifierForSnapshotting;
@property (Tq,R,N) accessibilityContrast;
@property (Tq,R,N) pointerLockStatus;
@property (Tq,R,N) interfaceOrientationMode;
@property (T@"<BSInterfaceOrientationMapResolving><BSXPCSecureCoding>",R,N) interfaceOrientationMapResolver;
@property (TB,R,N) screenBoundsIgnoresSceneOrientation;
@property (Tq,R,N) screenReferenceDisplayModeStatus;
@property (TB,R,N) enhancedWindowingEnabled;
@property (TQ,R,N) hostReferenceAngleMode;
@property (Td,R,N) angleFromHostReferenceUprightDirection;
@property (T@"NSSet",R,N) targetOfEventDeferringEnvironments;
@property (TB,R,N) inLiveResize;
@property (TB,R,N) isCapturingContentForAdditionalRenderingDestination;
@property (T@"AXFBFakeProcessState",&,N,V_state) state;
@property (T@"NSString",&,N,V_bundleIdentifier) bundleIdentifier;
@property (Ti,N,V_pid) pid;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSMutableDictionary",&,N,V_watchActiveWristState) watchActiveWristState;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (Ti,R,N,V_registrationMessageKey) registrationMessageKey;
@property (Ti,R,N,V_actionResultMessageKey) actionResultMessageKey;
```

## Strings (167)

```
applicationController
_accessibilityCachedWorkspaces
floatingDockController
event
_appProtectionCoordinator
searchBar-todayView
SBRemoteTransientOverlayViewController
v32@?0@\"FBProcess\"8Q16^B24
active device doesn't have auto answer enabled
  Scene Level: %@\n
isOccluded
GAXSpringboard
searchBar
bundleIdentifier
When getting frontmost apps, got %lu processes but %lu scenes.  Counts should have been equal.
serviceViewControllerClassName
isForeground
bundleIdentifiersToAssistants
shouldShield
NOT (bundleIdentifier == %@) AND NOT (bundleIdentifier == %@)
Accessibility reboot
BSKeyedSettings
com.apple.Siri
FrontBoardUtilsStrings
SBMainWorkspace
Unable to determine device on-wrist state
com.apple.DocumentManager.DockFolderViewService
Medusa
NO-SPOKEN-NAME
B32@?0@8Q16^B24
active device is not connected
CFBundleSpokenName
Using app with largest area as Speak Screen app: %@
topmostPresentedViewController
q24@?0@\"NSDictionary\"8@\"NSDictionary\"16
NO
  Scene Frame: %@\n
  Scene settings foreground: %@\n
v24@?0@\"FBScene\"8^B16
B32@?0@\"NSDictionary\"8Q16^B24
NSString
FBProcessManager
ahap
  Is foreground visible: %@\n
FBApplicationProcess
/Library/Caches/com.apple.xbs/1BFAFF86-4998-4057-B1A2-4FD228739DCE/TemporaryDirectory.2p9tYL/Sources/AccessibilityFrameworks/AccessibilityUmbrellaFramework/Frameworks/AXFrontBoardUtils/Source/AXFrontBoardUtils.m
NSArray * _Nonnull AXFrontBoardFocusedAppPIDs(void)
NSArray
true
no active, paired device
alr_preflightTargetScene
NSNumber * _Nullable AXFrontBoardSpeakThisAppPIDForPoint(NSValue *__strong _Nullable)
SBSpotlightTransientOverlayViewController
AX IDS connected devices: %@
v32@?0@\"NSDictionary\"8Q16^B24
q
  Scene ID: %@\n
AXFrontBoardFocusedAppPIDs() must be called on the main thread
transientOverlayPresentationManager
isRemoteContentPresenting
FBSScene
rootViewController
process
isInWorkspace
com.apple.UIKit.remote-keyboard
com.apple.DashBoard
PID:%ld <no other info available>
v8@?0
  Scene is Occluded: %@\n
FBScene
alr_activePreflightScene
no connected devices!
Finding the Speak Screen app for portrait-up coordinate: %@
activeDisplayWindowScene
identifier
FBProcess
SBAlertItemWindow
B16@?0@\"NSDictionary\"8
AXValidateFocusedApps
v16@?0@\"NSNotification\"8
register
PHEmergencyDialerViewController
FBSceneManager
presentedViewController
parentScene
payload
settings
com.apple.InputUI
Using system app as Speak Screen app
windowSceneManager
onWristState
received incoming IDS data: %@
AXFrontBoardCategoriesDidInstallNotification
AXValidateFocusedAppsEventAppStateVisibilityDidChange
terminated
type
UISceneHosting-com.apple.springboard
Allowing active watch to auto answer non-video call
UIAlertController
PID:%ld Name:%@ BundleID:%@
axserverinstance-action-queue
FBScene (AX) <%p>\n
  Is a UIApplication: %@\n
<_UIViewServiceSceneSettings>
clientProcess
systemApplicationProcess
remoteContentManager
  Scene Process (pid): %@\n
  Belongs to system app: %@\n
_legacyOtherSettings
visibility
clientHandle
scene
v32@?0@\"FBScene\"8Q16^B24
searchScreen
FBSceneClientHandle
com.apple.shortcuts.runtime
state
active device identifier: %@
frame
pid
Found app %@ which contained that point in its frame %@
YES
requesting watch on wrist state
taskState
ax_autoAnswer
  Is foreground running: %@\n
SBInCallTransientOverlayViewController
sharedInstanceIfExists
sharedInstance
_instanceIfExists
_hostContentAdapter.serviceBundleIdentifier
result
B32@?0@\"AXIPCClient\"8Q16^B24
level
Spotlight frontmost, but spotlight is not visible
Could not get transient process
  %@
Process state change:%@.\n From:%@\nTo:%@
Error sending server instance action: %@
failed to set audio session category (%@) due to: %@
failed to make haptic engine: %@
failed to play haptic: %@
top most alert service identifier: %@
%{public}@
 Previous:
 New:
auto answer safety asset playing, isSilentMode=%@
failed to set audio session active due to: %@
focused apps did change
Foreground Processes And Scenes: %@
Received focused app validation event: %s (%ld)
Could not connect client for registering serveri nstance action handler: %{public}@
System alert window: %@
Playing safety sound, call answer delay: %@
Auto-answering incoming call: %{public}@ , with status: %d
auto answer - played pattern: %@
Error fetching record: %@
Spotlight status: %d, %d %@
did initialize AXFrontBoardProcessWatcher
auto answer: should answer: %@
Auto Answer pref val is %{public}@ - call count is %lu, incoming call: %{public}@ , incoming video call: %{public}@
top most alert controller: %@
Filtering scene %@ (bundle: %@) — process foreground: %d, scene settings foreground: %d
System app process frontmost (app switcher: %d, passocde: %d
Including scene %@ (bundle: %@) — process foreground: YES, scene settings foreground: YES
Did add new process: %@\nState: %@
```
