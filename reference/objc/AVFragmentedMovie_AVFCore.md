# `AVFragmentedMovie`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVMovie`
- Protocols: `AVFragmentMinding`
- 0 instance variables, 2 properties, 10 instance methods, 1 class methods

## Properties

```
@property (T@"NSArray",R,N) tracks;
@property (TB,R,N,GisAssociatedWithFragmentMinder) associatedWithFragmentMinder;
```

## Class methods

```
+[AVFragmentedMovie expectsPropertyRevisedNotifications];
```

## Instance methods

```
-[AVFragmentedMovie isAssociatedWithFragmentMinder];
-[AVFragmentedMovie tracksWithMediaCharacteristic:];
-[AVFragmentedMovie tracksWithMediaType:];
-[AVFragmentedMovie initWithURL:options:];
-[AVFragmentedMovie trackWithTrackID:];
-[AVFragmentedMovie _setIsAssociatedWithFragmentMinder:];
-[AVFragmentedMovie tracks];
-[AVFragmentedMovie _mindsFragments];
-[AVFragmentedMovie _needsLegacyChangeNotifications];
-[AVFragmentedMovie _classForMovieTracks];
```
