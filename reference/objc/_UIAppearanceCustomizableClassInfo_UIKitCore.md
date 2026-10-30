# `_UIAppearanceCustomizableClassInfo`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 4 properties, 9 instance methods, 2 class methods

## Instance variables

```
B _isGuideClassRoot;
B _isCustomizableViewClassRoot;
@"NSString" _classReferenceKey;
Q _hash;
# _customizableViewClass;
# _guideClass;
```

## Properties

```
@property (T#,R,N,V_customizableViewClass) _customizableViewClass;
@property (T#,R,N,V_guideClass) _guideClass;
@property (T@"NSString",R,N,V_classReferenceKey) _classReferenceKey;
@property (TQ,R,N,V_hash) _hash;
```

## Class methods

```
+[_UIAppearanceCustomizableClassInfo _cachedClassInfoForViewClass:withGuideClass:];
+[_UIAppearanceCustomizableClassInfo _customizableClassInfoForViewClass:withGuideClass:];
```

## Instance methods

```
-[_UIAppearanceCustomizableClassInfo _hash];
-[_UIAppearanceCustomizableClassInfo dealloc];
-[_UIAppearanceCustomizableClassInfo _guideClass];
-[_UIAppearanceCustomizableClassInfo _superClassInfo];
-[_UIAppearanceCustomizableClassInfo hash];
-[_UIAppearanceCustomizableClassInfo _classReferenceKey];
-[_UIAppearanceCustomizableClassInfo _customizableViewClass];
-[_UIAppearanceCustomizableClassInfo description];
-[_UIAppearanceCustomizableClassInfo isEqual:];
```
