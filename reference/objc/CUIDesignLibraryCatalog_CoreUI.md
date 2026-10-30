# `CUIDesignLibraryCatalog`

- Image: [`/System/Library/PrivateFrameworks/CoreUI.framework/CoreUI`](../userland/System__Library__PrivateFrameworks__CoreUI.framework__CoreUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 4 properties, 15 instance methods, 3 class methods

## Instance variables

```
Q _storageRef;
@"NSString" _assetStoreName;
[5[28[4@]]] _colorCache;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
q _designSystem;
q _colorScheme;
q _contrast;
q _styling;
```

## Properties

```
@property (Tq,V_designSystem) designSystem;
@property (Tq,V_colorScheme) colorScheme;
@property (Tq,V_contrast) contrast;
@property (Tq,V_styling) styling;
```

## Class methods

```
+[CUIDesignLibraryCatalog catalogForDesignSystem:colorScheme:contrast:styling:error:];
+[CUIDesignLibraryCatalog _bundleNameForResolvedDesignSystem:];
+[CUIDesignLibraryCatalog _catalogPathComponentForDesignSystem:colorScheme:contrast:styling:error:];
```

## Instance methods

```
-[CUIDesignLibraryCatalog setContrast:];
-[CUIDesignLibraryCatalog setColorScheme:];
-[CUIDesignLibraryCatalog colorScheme];
-[CUIDesignLibraryCatalog dealloc];
-[CUIDesignLibraryCatalog _colorNameStringFromNameEnum:palette:];
-[CUIDesignLibraryCatalog shapeEffectPresetWithName:error:];
-[CUIDesignLibraryCatalog setDesignSystem:];
-[CUIDesignLibraryCatalog contrast];
-[CUIDesignLibraryCatalog initWithURL:error:];
-[CUIDesignLibraryCatalog description];
-[CUIDesignLibraryCatalog designSystem];
-[CUIDesignLibraryCatalog styling];
-[CUIDesignLibraryCatalog colorWithName:palette:displayGamut:error:];
-[CUIDesignLibraryCatalog colorWithName:palette:displayGamut:hierarchyLevel:error:];
-[CUIDesignLibraryCatalog setStyling:];
```
