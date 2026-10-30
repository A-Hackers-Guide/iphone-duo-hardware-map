# `UISearchBarBackground`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIBarBackgroundImageView`
- Protocols: `_UIBarPositioningInternal`
- 8 instance variables, 12 properties, 27 instance methods, 0 class methods

## Instance variables

```
@"UIColor" _barTintColor;
@"NSMutableDictionary" _customBackgroundImages;
q _barPosition;
Q _searchBarStyle;
q _barStyle;
q _barTranslucence;
B _usesEmbeddedAppearance;
B _usesContiguousBarBackground;
```

## Properties

```
@property (Tq,N) barStyle;
@property (TQ,N) searchBarStyle;
@property (T@"UIColor",&,N,V_barTintColor) barTintColor;
@property (TB,N,GisTranslucent) translucent;
@property (TB,N) usesEmbeddedAppearance;
@property (T@"UIImage",R,N) backgroundImage;
@property (T@"UIImage",R,N) backgroundImagePrompt;
@property (TB,N) usesContiguousBarBackground;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UISearchBarBackground setSearchBarStyle:];
-[UISearchBarBackground _setBackgroundImage:forBarPosition:barMetrics:];
-[UISearchBarBackground didMoveToWindow];
-[UISearchBarBackground _dynamicUserInterfaceTraitDidChange];
-[UISearchBarBackground _hasCustomBackgroundImage];
-[UISearchBarBackground backgroundImage];
-[UISearchBarBackground _createBackgroundImageForBarStyle:alpha:];
-[UISearchBarBackground setBarTintColor:];
-[UISearchBarBackground setTranslucent:];
-[UISearchBarBackground barStyle];
-[UISearchBarBackground usesEmbeddedAppearance];
-[UISearchBarBackground setBounds:];
-[UISearchBarBackground _updateBackgroundImageIfPossible];
-[UISearchBarBackground setUsesContiguousBarBackground:];
-[UISearchBarBackground setBarStyle:];
-[UISearchBarBackground isTranslucent];
-[UISearchBarBackground _updateBackgroundImage];
-[UISearchBarBackground setFrame:];
-[UISearchBarBackground backgroundImagePrompt];
-[UISearchBarBackground _backgroundImageForBarPosition:barMetrics:];
-[UISearchBarBackground barTintColor];
-[UISearchBarBackground setUsesEmbeddedAppearance:];
-[UISearchBarBackground _setBarPosition:];
-[UISearchBarBackground initWithFrame:];
-[UISearchBarBackground usesContiguousBarBackground];
-[UISearchBarBackground searchBarStyle];
-[UISearchBarBackground _barPosition];
```
