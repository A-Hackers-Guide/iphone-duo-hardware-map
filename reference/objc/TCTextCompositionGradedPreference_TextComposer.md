# `TCTextCompositionGradedPreference`

- Image: [`/System/Library/PrivateFrameworks/TextComposer.framework/TextComposer`](../userland/System__Library__PrivateFrameworks__TextComposer.framework__TextComposer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 4 instance variables, 4 properties, 10 instance methods, 1 class methods

## Instance variables

```
@"NSString" _preferenceString;
q _maxGrade;
q _minGrade;
@"NSNumber" _chosenGrade;
```

## Properties

```
@property (T@"NSString",R,C,V_preferenceString) preferenceString;
@property (Tq,R,V_maxGrade) maxGrade;
@property (Tq,R,V_minGrade) minGrade;
@property (T@"NSNumber",R,C,V_chosenGrade) chosenGrade;
```

## Class methods

```
+[TCTextCompositionGradedPreference supportsSecureCoding];
```

## Instance methods

```
-[TCTextCompositionGradedPreference preferenceString];
-[TCTextCompositionGradedPreference encodeWithCoder:];
-[TCTextCompositionGradedPreference hash];
-[TCTextCompositionGradedPreference initWithCoder:];
-[TCTextCompositionGradedPreference copyWithZone:];
-[TCTextCompositionGradedPreference isEqual:];
-[TCTextCompositionGradedPreference chosenGrade];
-[TCTextCompositionGradedPreference initWithPrefenceString:maxGrade:minGrade:chosenGrade:];
-[TCTextCompositionGradedPreference maxGrade];
-[TCTextCompositionGradedPreference minGrade];
```
