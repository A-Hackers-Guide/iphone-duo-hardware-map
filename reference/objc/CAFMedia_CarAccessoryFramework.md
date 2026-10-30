# `CAFMedia`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFAccessory`
- 0 instance variables, 2 properties, 12 instance methods, 2 class methods

## Properties

```
@property (T@"NSArray",R,N) mediaSourceServices;
@property (T@"NSArray",R,N) mediaSources;
```

## Class methods

```
+[CAFMedia accessoryIdentifier];
+[CAFMedia observerProtocol];
```

## Instance methods

```
-[CAFMedia removeObserver:];
-[CAFMedia addObserver:];
-[CAFMedia registerObserver:];
-[CAFMedia unregisterObserver:];
-[CAFMedia mediaSources];
-[CAFMedia tuneToFrequency:inSourceWithIdentifier:completion:];
-[CAFMedia tuneToMediaItem:inSource:completion:];
-[CAFMedia mediaSourceServices];
-[CAFMedia tuneToFrequency:inSourceWithIdentifier:multicastIndex:completion:];
-[CAFMedia tuneToMediaItem:inSource:multicastIndex:completion:];
-[CAFMedia tuneToMediaItemIdentifier:inSourceWithIdentifier:completion:];
-[CAFMedia tuneToMediaItemIdentifier:inSourceWithIdentifier:multicastIndex:completion:];
```
