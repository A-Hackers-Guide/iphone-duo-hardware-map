# `CSEntityHosting` (protocol)

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 3 properties, 5 instance methods, 0 class methods

## Properties

```
@property (T@"<CSHostableEntity>",R,N) hostedEntity;
@property (T@"<BSInvalidatable>",?,&,N) entityPreservationToken;
@property (T@"NSSet",?,&,N) actionsToDeliver;
```

## Instance methods

```
-[CSEntityHosting hostedEntity];
-[CSEntityHosting actionsToDeliver];
-[CSEntityHosting setActionsToDeliver:];
-[CSEntityHosting entityPreservationToken];
-[CSEntityHosting setEntityPreservationToken:];
```
