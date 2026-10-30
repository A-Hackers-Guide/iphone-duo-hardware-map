# `SBKeyboardFocusPolicy`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionStreaming`, `NSCopying`, `NSMutableCopying`
- 6 instance variables, 10 properties, 14 instance methods, 2 class methods

## Instance variables

```
@"SBKeyboardFocusTarget" _keyboardFocusTarget;
q _selectionPolicy;
B _shouldSuppressRemoteDeferring;
B _suppressCameraButtonDeferringToApplications;
@"BSAuditHistory" _auditHistory;
@"SBWindowScene" _sbWindowSceneAncestor;
```

## Properties

```
@property (T@"BSAuditHistory",R,N) auditHistory;
@property (T@"SBKeyboardFocusTarget",R,N) keyboardFocusTarget;
@property (Tq,R,N) advicePolicy;
@property (TB,R,N) shouldSuppressRemoteDeferring;
@property (TB,R,N) suppressCameraButtonDeferringToApplications;
@property (T@"SBWindowScene",R,W,N) sbWindowSceneAncestor;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBKeyboardFocusPolicy build:];
+[SBKeyboardFocusPolicy new];
```

## Instance methods

```
-[SBKeyboardFocusPolicy mutableCopyWithZone:];
-[SBKeyboardFocusPolicy debugDescription];
-[SBKeyboardFocusPolicy init];
-[SBKeyboardFocusPolicy keyboardFocusTarget];
-[SBKeyboardFocusPolicy hash];
-[SBKeyboardFocusPolicy description];
-[SBKeyboardFocusPolicy appendDescriptionToStream:];
-[SBKeyboardFocusPolicy copyWithZone:];
-[SBKeyboardFocusPolicy auditHistory];
-[SBKeyboardFocusPolicy isEqual:];
-[SBKeyboardFocusPolicy advicePolicy];
-[SBKeyboardFocusPolicy sbWindowSceneAncestor];
-[SBKeyboardFocusPolicy shouldSuppressRemoteDeferring];
-[SBKeyboardFocusPolicy suppressCameraButtonDeferringToApplications];
```
