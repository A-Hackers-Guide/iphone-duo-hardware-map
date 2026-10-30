# `UIImageConfiguration`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIImageConfiguration`, `NSCopying`, `NSSecureCoding`
- 4 instance variables, 9 properties, 24 instance methods, 4 class methods

## Instance variables

```
{?="hasSystemIconAppearance"b1} _flags;
B _ignoresDynamicType;
@"UITraitCollection" _traitCollection;
@"NSLocale" _locale;
```

## Properties

```
@property (T@"_UISystemIconAppearance",R,N) _systemIconAppearance;
@property (T@"UITraitCollection",R,N) _effectiveTraitCollectionForImageLookup;
@property (TB,R,N,V_ignoresDynamicType) _ignoresDynamicType;
@property (T@"UITraitCollection",R,N,V_traitCollection) traitCollection;
@property (T@"NSLocale",R,N,V_locale) locale;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIImageConfiguration supportsSecureCoding];
+[UIImageConfiguration configurationWithLocale:];
+[UIImageConfiguration configurationWithTraitCollection:];
+[UIImageConfiguration _unspecifiedConfiguration];
```

## Instance methods

```
-[UIImageConfiguration _ignoresDynamicType];
-[UIImageConfiguration _configurationWithSystemIconAppearance:];
-[UIImageConfiguration _shouldApplyConfiguration:];
-[UIImageConfiguration isEqualToConfiguration:];
-[UIImageConfiguration _isEquivalentToConfiguration:];
-[UIImageConfiguration configurationWithLocale:];
-[UIImageConfiguration configurationWithTraitCollection:];
-[UIImageConfiguration _systemIconAppearance];
-[UIImageConfiguration _initWithTraitCollection:];
-[UIImageConfiguration _isUnspecified];
-[UIImageConfiguration traitCollection];
-[UIImageConfiguration debugDescription];
-[UIImageConfiguration _effectiveTraitCollectionForImageLookup];
-[UIImageConfiguration _applyConfigurationValuesTo:];
-[UIImageConfiguration _init];
-[UIImageConfiguration locale];
-[UIImageConfiguration encodeWithCoder:];
-[UIImageConfiguration hash];
-[UIImageConfiguration description];
-[UIImageConfiguration initWithCoder:];
-[UIImageConfiguration copyWithZone:];
-[UIImageConfiguration isEqual:];
-[UIImageConfiguration configurationByApplyingConfiguration:];
-[UIImageConfiguration _configurationIgnoringDynamicType];
```
