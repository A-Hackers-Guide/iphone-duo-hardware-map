# `AVTextStyleRule`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 1 instance variables, 2 properties, 10 instance methods, 4 class methods

## Instance variables

```
@"AVTextStyleRuleInternal" _textStyleRule;
```

## Properties

```
@property (T@"NSDictionary",R,N) textMarkupAttributes;
@property (T@"NSString",R,N) textSelector;
```

## Class methods

```
+[AVTextStyleRule textStyleRulesFromPropertyList:];
+[AVTextStyleRule propertyListForTextStyleRules:];
+[AVTextStyleRule textStyleRuleWithTextMarkupAttributes:];
+[AVTextStyleRule textStyleRuleWithTextMarkupAttributes:textSelector:];
```

## Instance methods

```
-[AVTextStyleRule init];
-[AVTextStyleRule dealloc];
-[AVTextStyleRule hash];
-[AVTextStyleRule copyWithZone:];
-[AVTextStyleRule isEqual:];
-[AVTextStyleRule _dictionaryPlistRepresentation];
-[AVTextStyleRule initWithTextMarkupAttributes:];
-[AVTextStyleRule initWithTextMarkupAttributes:textSelector:];
-[AVTextStyleRule textMarkupAttributes];
-[AVTextStyleRule textSelector];
```
