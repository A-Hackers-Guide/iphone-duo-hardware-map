# `SBPlatterHomeGestureManager`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBPlatterHomeGestureContextDelegate`
- 2 instance variables, 5 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"NSMapTable" _participantsToHomeGestureContexts;
@"<SBPlatterHomeGestureManagerDelegate>" _delegate;
```

## Properties

```
@property (T@"<SBPlatterHomeGestureManagerDelegate>",R,W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBPlatterHomeGestureManager initWithDelegate:];
-[SBPlatterHomeGestureManager delegate];
-[SBPlatterHomeGestureManager _allParticipants];
-[SBPlatterHomeGestureManager _homeGestureContextForParticipant:creatingIfNecessary:withWindowScene:];
-[SBPlatterHomeGestureManager _participantForHomeGestureContext:];
-[SBPlatterHomeGestureManager _removeHomeGestureContextForParticipant:];
-[SBPlatterHomeGestureManager bannerManagerHomeGestureContext:homeGestureOwnershipDidChange:];
-[SBPlatterHomeGestureManager gestureRecognizerPriorityAssertionForBannerManagerHomeGestureContext:];
-[SBPlatterHomeGestureManager keyboardHomeAffordanceAssertionForBannerManagerHomeGestureContext:];
-[SBPlatterHomeGestureManager registerParticipant:windowScene:];
-[SBPlatterHomeGestureManager unregisterParticipant:];
-[SBPlatterHomeGestureManager wantsHomeGestureDidChangeForBannerManagerHomeGestureContext:];
```
