# `AVMediaPresentationSelector`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 3 instance variables, 2 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"NSString" _identifier;
@"NSArray" _mediaPresentationSettings;
@"NSDictionary" _displayNames;
```

## Properties

```
@property (T@"NSString",R) identifier;
@property (T@"NSArray",R) settings;
```

## Instance methods

```
-[AVMediaPresentationSelector identifier];
-[AVMediaPresentationSelector settings];
-[AVMediaPresentationSelector dealloc];
-[AVMediaPresentationSelector hash];
-[AVMediaPresentationSelector description];
-[AVMediaPresentationSelector copyWithZone:];
-[AVMediaPresentationSelector isEqual:];
-[AVMediaPresentationSelector displayNameForLocaleIdentifier:];
-[AVMediaPresentationSelector _settingsSatisfiableByOptions:];
-[AVMediaPresentationSelector _settingsSatisfiableByOptions:satisfiableLanguages:];
-[AVMediaPresentationSelector initWithFigAssetCustomMediaSelectionSchemeSelector:];
```
