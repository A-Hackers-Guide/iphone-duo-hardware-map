# `_UIPasteboardOptions`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 7 instance methods, 1 class methods

## Instance variables

```
B _pinned;
B _localOnly;
@"NSDate" _expirationDate;
```

## Properties

```
@property (TB,N,GisPinned,V_pinned) pinned;
@property (TB,N,GisLocalOnly,V_localOnly) localOnly;
@property (T@"NSDate",&,N,V_expirationDate) expirationDate;
```

## Class methods

```
+[_UIPasteboardOptions optionsWithDictionary:];
```

## Instance methods

```
-[_UIPasteboardOptions setPinned:];
-[_UIPasteboardOptions isPinned];
-[_UIPasteboardOptions expirationDate];
-[_UIPasteboardOptions setLocalOnly:];
-[_UIPasteboardOptions initWithOptionsDictionary:];
-[_UIPasteboardOptions setExpirationDate:];
-[_UIPasteboardOptions isLocalOnly];
```
