# `SBFHomeAffordanceInteraction` (protocol)

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `UIInteraction`
- 0 instance variables, 3 properties, 6 instance methods, 0 class methods

## Properties

```
@property (T@"<SBFHomeAffordanceInteractionDelegate>",W,N) delegate;
@property (TB,N,GisEnabled) enabled;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) homeAffordanceHitTestRect;
```

## Instance methods

```
-[SBFHomeAffordanceInteraction isEnabled];
-[SBFHomeAffordanceInteraction setDelegate:];
-[SBFHomeAffordanceInteraction setEnabled:];
-[SBFHomeAffordanceInteraction delegate];
-[SBFHomeAffordanceInteraction homeAffordanceHitTestRect];
-[SBFHomeAffordanceInteraction setNeedsUpdate];
```
