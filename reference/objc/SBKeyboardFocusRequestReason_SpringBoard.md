# `SBKeyboardFocusRequestReason`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 1 properties, 6 instance methods, 13 class methods

## Instance variables

```
@"NSString" _name;
```

## Properties

```
@property (T@"NSString",R,C,N,V_name) name;
```

## Class methods

```
+[SBKeyboardFocusRequestReason homeScreenVisible];
+[SBKeyboardFocusRequestReason splitPictureInPicture];
+[SBKeyboardFocusRequestReason switcherAddedMultipleApps];
+[SBKeyboardFocusRequestReason switcherAddedSingleApp];
+[SBKeyboardFocusRequestReason switcherFocusedWindowClosed];
+[SBKeyboardFocusRequestReason switcherHomeScreenTouchDown];
+[SBKeyboardFocusRequestReason switcherInflexibleWindowingAppForeground];
+[SBKeyboardFocusRequestReason switcherLayoutChangeRequests];
+[SBKeyboardFocusRequestReason switcherRotationCollapsedStage];
+[SBKeyboardFocusRequestReason switcherRotationRestoredStage];
+[SBKeyboardFocusRequestReason switcherSplitAppTouchDown];
+[SBKeyboardFocusRequestReason switcherTransitionDeferringRuleCreated];
+[SBKeyboardFocusRequestReason switcherUpdateTopmostApp];
```

## Instance methods

```
-[SBKeyboardFocusRequestReason hash];
-[SBKeyboardFocusRequestReason description];
-[SBKeyboardFocusRequestReason isEqual:];
-[SBKeyboardFocusRequestReason name];
-[SBKeyboardFocusRequestReason initWithName:];
-[SBKeyboardFocusRequestReason matchesReason:];
```
