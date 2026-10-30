# `AVDelegatingPlaybackCoordinatorBufferingCommand`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVDelegatingPlaybackCoordinatorPlaybackControlCommand`
- 6 instance variables, 2 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"AVDelegatingPlaybackCoordinator" _coordinator;
@"AVCoordinatedPlaybackParticipant" _originator;
@"NSString" _expectedCurrentItemIdentifier;
q _commandOrderIndex;
f _anticipatedPlaybackRate;
@"NSDate" _completionDueDate;
```

## Properties

```
@property (Tf,R,N,V_anticipatedPlaybackRate) anticipatedPlaybackRate;
@property (T@"NSDate",R,N,V_completionDueDate) completionDueDate;
```

## Instance methods

```
-[AVDelegatingPlaybackCoordinatorBufferingCommand init];
-[AVDelegatingPlaybackCoordinatorBufferingCommand dealloc];
-[AVDelegatingPlaybackCoordinatorBufferingCommand originator];
-[AVDelegatingPlaybackCoordinatorBufferingCommand anticipatedPlaybackRate];
-[AVDelegatingPlaybackCoordinatorBufferingCommand completionDueDate];
-[AVDelegatingPlaybackCoordinatorBufferingCommand expectedCurrentItemIdentifier];
-[AVDelegatingPlaybackCoordinatorBufferingCommand initWithCoordinator:originator:expectedCurrentItemIdentifier:commandOrderIndex:anticipatedPlaybackRate:completionDueDate:];
```
