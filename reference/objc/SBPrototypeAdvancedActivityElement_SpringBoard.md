# `SBPrototypeAdvancedActivityElement`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBPrototypeAdvancedActivityElementViewProviderDelegate`, `SBSystemApertureElement`, `SAActivityBehavior`
- 3 instance variables, 9 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"NSMapTable" _viewProvidersByToken;
@"<SAElementHosting>" _elementHost;
@"<SBSystemAperturePlatformElementHosting>" _platformElementHost;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<SBSystemAperturePlatformElementHosting>",?,W,N,V_platformElementHost) platformElementHost;
@property (T@"<SAElementHosting>",?,W,N,V_elementHost) elementHost;
@property (T@"NSString",R,C,N) clientIdentifier;
@property (T@"NSString",R,C,N) elementIdentifier;
@property (T@"<SAActivityHosting>",?,W,N) activityHost;
```

## Instance methods

```
-[SBPrototypeAdvancedActivityElement clientIdentifier];
-[SBPrototypeAdvancedActivityElement elementIdentifier];
-[SBPrototypeAdvancedActivityElement init];
-[SBPrototypeAdvancedActivityElement setPlatformElementHost:];
-[SBPrototypeAdvancedActivityElement elementHost];
-[SBPrototypeAdvancedActivityElement hasActivityBehavior];
-[SBPrototypeAdvancedActivityElement setElementHost:];
-[SBPrototypeAdvancedActivityElement platformElementHost];
-[SBPrototypeAdvancedActivityElement viewProviderForDestinationToken:];
-[SBPrototypeAdvancedActivityElement viewProviderRequestsSignificantUpdateTransition:];
```
