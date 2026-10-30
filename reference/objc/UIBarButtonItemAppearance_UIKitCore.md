# `UIBarButtonItemAppearance`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 3 instance variables, 7 properties, 29 instance methods, 1 class methods

## Instance variables

```
@"<_UIBarButtonItemAppearanceChangeObserver>" _changeObserver;
@"_UIBarButtonItemData" _data;
[4@"UIBarButtonItemStateAppearance"] _states;
```

## Properties

```
@property (T@"_UIBarButtonItemData",R,N,V_data) _data;
@property (T@"<_UIBarButtonItemAppearanceChangeObserver>",W,N,S_setChangeObserver:,V_changeObserver) _changeObserver;
@property (T@"<_UIBarButtonItemDataFallback>",&,N,S_setFallback:) _fallback;
@property (T@"UIBarButtonItemStateAppearance",R,N) normal;
@property (T@"UIBarButtonItemStateAppearance",R,N) highlighted;
@property (T@"UIBarButtonItemStateAppearance",R,N) disabled;
@property (T@"UIBarButtonItemStateAppearance",R,N) focused;
```

## Class methods

```
+[UIBarButtonItemAppearance supportsSecureCoding];
```

## Instance methods

```
-[UIBarButtonItemAppearance disabled];
-[UIBarButtonItemAppearance normal];
-[UIBarButtonItemAppearance focused];
-[UIBarButtonItemAppearance init];
-[UIBarButtonItemAppearance copy];
-[UIBarButtonItemAppearance dealloc];
-[UIBarButtonItemAppearance configureWithDefaultForStyle:];
-[UIBarButtonItemAppearance highlighted];
-[UIBarButtonItemAppearance initWithBarButtonItemAppearance:];
-[UIBarButtonItemAppearance initWithStyle:];
-[UIBarButtonItemAppearance _describeInto:];
-[UIBarButtonItemAppearance _setData:];
-[UIBarButtonItemAppearance _updateToSupportBackIndicatorsCopyingIndicatorsAndFallbackFrom:];
-[UIBarButtonItemAppearance _resetBackIndicatorImages];
-[UIBarButtonItemAppearance _setFallback:];
-[UIBarButtonItemAppearance _updateDataTo:signal:];
-[UIBarButtonItemAppearance _data];
-[UIBarButtonItemAppearance _changeObserver];
-[UIBarButtonItemAppearance encodeWithCoder:];
-[UIBarButtonItemAppearance _proxyForState:];
-[UIBarButtonItemAppearance hash];
-[UIBarButtonItemAppearance description];
-[UIBarButtonItemAppearance initWithCoder:];
-[UIBarButtonItemAppearance _setBackIndicatorImage:transitionMaskImage:];
-[UIBarButtonItemAppearance copyWithZone:];
-[UIBarButtonItemAppearance _fallback];
-[UIBarButtonItemAppearance isEqual:];
-[UIBarButtonItemAppearance _writeToStorage:];
-[UIBarButtonItemAppearance _setChangeObserver:];
```
