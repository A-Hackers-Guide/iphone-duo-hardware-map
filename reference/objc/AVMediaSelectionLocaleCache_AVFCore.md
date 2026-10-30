# `AVMediaSelectionLocaleCache`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 1 properties, 4 instance methods, 1 class methods

## Instance variables

```
^{OpaqueFigSimpleMutex=} _mutex;
@"NSString" _preferredLocalizationLanguage;
```

## Properties

```
@property (T@"NSString",R,C) preferredLocalizationLanguage;
```

## Class methods

```
+[AVMediaSelectionLocaleCache singleton];
```

## Instance methods

```
-[AVMediaSelectionLocaleCache init];
-[AVMediaSelectionLocaleCache dealloc];
-[AVMediaSelectionLocaleCache _updateCache];
-[AVMediaSelectionLocaleCache preferredLocalizationLanguage];
```
