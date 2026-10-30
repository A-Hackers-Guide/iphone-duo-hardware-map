# `CUINamedColor`

- Image: [`/System/Library/PrivateFrameworks/CoreUI.framework/CoreUI`](../userland/System__Library__PrivateFrameworks__CoreUI.framework__CoreUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CUINamedLookup`
- 3 instance variables, 3 properties, 7 instance methods, 0 class methods

## Instance variables

```
^{CGColor=} _cgColor;
@"NSString" _colorName;
B _substituteWithSystemColor;
```

## Properties

```
@property (T^{CGColor=},R,N) cgColor;
@property (TB,R,N,V_substituteWithSystemColor) substituteWithSystemColor;
@property (T@"NSString",R,N,V_colorName) systemColorName;
```

## Instance methods

```
-[CUINamedColor dealloc];
-[CUINamedColor systemColorName];
-[CUINamedColor cgColor];
-[CUINamedColor initWithName:usingRenditionKey:fromTheme:];
-[CUINamedColor mutableCopy];
-[CUINamedColor substituteWithSystemColor];
-[CUINamedColor _setCGColor:];
```
