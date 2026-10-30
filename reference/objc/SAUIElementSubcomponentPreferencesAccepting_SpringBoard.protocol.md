# `SAUIElementSubcomponentPreferencesAccepting` (protocol)

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `SAUIElementSubcomponentPreferencesProviding`
- 0 instance variables, 20 properties, 40 instance methods, 0 class methods

## Properties

```
@property (Td,N) leadingViewBlurProgress;
@property (Td,N) leadingViewAlpha;
@property (Td,N) leadingViewSquishProgress;
@property (T{CGSize=dd},N) leadingViewScale;
@property (Td,N) trailingViewBlurProgress;
@property (Td,N) trailingViewAlpha;
@property (Td,N) trailingViewSquishProgress;
@property (T{CGSize=dd},N) trailingViewScale;
@property (Td,N) minimalViewBlurProgress;
@property (Td,N) minimalViewAlpha;
@property (Td,N) minimalViewSquishProgress;
@property (T{CGSize=dd},N) minimalViewScale;
@property (Td,N) customContentBlurProgress;
@property (Td,N) customContentAlpha;
@property (Td,N) snapshotViewBlurProgress;
@property (Td,N) snapshotViewAlpha;
@property (T{CGAffineTransform=dddddd},?,N) leadingViewTransform;
@property (T{CGAffineTransform=dddddd},?,N) trailingViewTransform;
@property (T{CGAffineTransform=dddddd},?,N) minimalViewTransform;
@property (T{CGAffineTransform=dddddd},?,N) customViewTransform;
```

## Instance methods

```
-[SAUIElementSubcomponentPreferencesAccepting minimalViewSquishProgress];
-[SAUIElementSubcomponentPreferencesAccepting leadingViewScale];
-[SAUIElementSubcomponentPreferencesAccepting leadingViewBlurProgress];
-[SAUIElementSubcomponentPreferencesAccepting setSnapshotViewBlurProgress:];
-[SAUIElementSubcomponentPreferencesAccepting setTrailingViewScale:];
-[SAUIElementSubcomponentPreferencesAccepting trailingViewAlpha];
-[SAUIElementSubcomponentPreferencesAccepting setMinimalViewSquishProgress:];
-[SAUIElementSubcomponentPreferencesAccepting customContentBlurProgress];
-[SAUIElementSubcomponentPreferencesAccepting setTrailingViewBlurProgress:];
-[SAUIElementSubcomponentPreferencesAccepting leadingViewAlpha];
-[SAUIElementSubcomponentPreferencesAccepting trailingViewSquishProgress];
-[SAUIElementSubcomponentPreferencesAccepting snapshotViewAlpha];
-[SAUIElementSubcomponentPreferencesAccepting setSnapshotViewAlpha:];
-[SAUIElementSubcomponentPreferencesAccepting setLeadingViewBlurProgress:];
-[SAUIElementSubcomponentPreferencesAccepting setLeadingViewAlpha:];
-[SAUIElementSubcomponentPreferencesAccepting setLeadingViewScale:];
-[SAUIElementSubcomponentPreferencesAccepting minimalViewAlpha];
-[SAUIElementSubcomponentPreferencesAccepting minimalViewScale];
-[SAUIElementSubcomponentPreferencesAccepting setTrailingViewSquishProgress:];
-[SAUIElementSubcomponentPreferencesAccepting setLeadingViewSquishProgress:];
-[SAUIElementSubcomponentPreferencesAccepting snapshotViewBlurProgress];
-[SAUIElementSubcomponentPreferencesAccepting customContentAlpha];
-[SAUIElementSubcomponentPreferencesAccepting setCustomContentBlurProgress:];
-[SAUIElementSubcomponentPreferencesAccepting setTrailingViewAlpha:];
-[SAUIElementSubcomponentPreferencesAccepting setMinimalViewBlurProgress:];
-[SAUIElementSubcomponentPreferencesAccepting setCustomContentAlpha:];
-[SAUIElementSubcomponentPreferencesAccepting setMinimalViewAlpha:];
-[SAUIElementSubcomponentPreferencesAccepting trailingViewBlurProgress];
-[SAUIElementSubcomponentPreferencesAccepting trailingViewScale];
-[SAUIElementSubcomponentPreferencesAccepting setMinimalViewScale:];
-[SAUIElementSubcomponentPreferencesAccepting minimalViewBlurProgress];
-[SAUIElementSubcomponentPreferencesAccepting leadingViewSquishProgress];
-[SAUIElementSubcomponentPreferencesAccepting setMinimalViewTransform:];
-[SAUIElementSubcomponentPreferencesAccepting leadingViewTransform];
-[SAUIElementSubcomponentPreferencesAccepting setLeadingViewTransform:];
-[SAUIElementSubcomponentPreferencesAccepting setTrailingViewTransform:];
-[SAUIElementSubcomponentPreferencesAccepting minimalViewTransform];
-[SAUIElementSubcomponentPreferencesAccepting trailingViewTransform];
-[SAUIElementSubcomponentPreferencesAccepting customViewTransform];
-[SAUIElementSubcomponentPreferencesAccepting setCustomViewTransform:];
```
