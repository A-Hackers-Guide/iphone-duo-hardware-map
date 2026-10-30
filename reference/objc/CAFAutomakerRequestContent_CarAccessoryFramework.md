# `CAFAutomakerRequestContent`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFAccessory`
- 0 instance variables, 4 properties, 8 instance methods, 2 class methods

## Properties

```
@property (T@"NSArray",R,N) requestContentServices;
@property (T@"NSArray",R,N) requestTemporaryContentServices;
@property (T@"NSArray",R,N) requestContents;
@property (T@"NSArray",R,N) requestTemporaryContents;
```

## Class methods

```
+[CAFAutomakerRequestContent accessoryIdentifier];
+[CAFAutomakerRequestContent observerProtocol];
```

## Instance methods

```
-[CAFAutomakerRequestContent removeObserver:];
-[CAFAutomakerRequestContent addObserver:];
-[CAFAutomakerRequestContent registerObserver:];
-[CAFAutomakerRequestContent unregisterObserver:];
-[CAFAutomakerRequestContent requestContents];
-[CAFAutomakerRequestContent requestTemporaryContents];
-[CAFAutomakerRequestContent requestTemporaryContentServices];
-[CAFAutomakerRequestContent requestContentServices];
```
