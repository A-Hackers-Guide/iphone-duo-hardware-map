# `SBMagSafeSleeveController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBFZStackParticipantDelegate`, `SBWindowedAccessoryViewControllerDelegate`
- 7 instance variables, 8 properties, 20 instance methods, 0 class methods

## Instance variables

```
b1 _isConnectedToWindowedAccessory;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _visibleScreenCoordinatesForWindowedAccessory;
@"<BSInvalidatable>" _suspendProximityForAttachedWindowedAccessoryAssertion;
@"SBFZStackParticipant" _zStackParticipant;
@"SBWindow" _window;
@"SBWindowScene" _windowScene;
@"SBWindowedAccessoryViewController" _windowedAccessoryViewController;
```

## Properties

```
@property (T@"SBWindowScene",R,W,N,V_windowScene) windowScene;
@property (T@"SBWindow",R,N,V_window) window;
@property (TB,R,N,GisWindowedAccessoryWindowVisible) windowedAccessoryWindowVisible;
@property (T@"SBWindowedAccessoryViewController",&,N,V_windowedAccessoryViewController) windowedAccessoryViewController;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBMagSafeSleeveController zStackParticipant:updatePreferences:];
-[SBMagSafeSleeveController window];
-[SBMagSafeSleeveController zStackParticipantDidChange:];
-[SBMagSafeSleeveController zStackParticipant:updateZOrderPreferences:];
-[SBMagSafeSleeveController initWithWindowScene:];
-[SBMagSafeSleeveController windowScene];
-[SBMagSafeSleeveController windowedAccessoryViewController];
-[SBMagSafeSleeveController _setConnectedToWindowedAccessory:];
-[SBMagSafeSleeveController _showWindowedAccessoryWindow:forWindowScene:];
-[SBMagSafeSleeveController _windowedAccessoryDismissed];
-[SBMagSafeSleeveController isConnectedToWindowedAccessory];
-[SBMagSafeSleeveController isWindowedAccessoryWindowVisible];
-[SBMagSafeSleeveController setWindowedAccessoryViewController:];
-[SBMagSafeSleeveController showWindowedAccessoryWindow:forWindowScene:];
-[SBMagSafeSleeveController visibleScreenCoordinatesForWindowedAccessory];
-[SBMagSafeSleeveController windowedAccessoryAttached:];
-[SBMagSafeSleeveController windowedAccessoryDismissed];
-[SBMagSafeSleeveController windowedAccessoryDismissed:];
-[SBMagSafeSleeveController windowedAccessoryPresented];
-[SBMagSafeSleeveController windowedAccessoryViewControllerForceDetachButtonTapped:];
```
