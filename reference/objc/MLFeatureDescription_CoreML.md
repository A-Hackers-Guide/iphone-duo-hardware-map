# `MLFeatureDescription`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 9 instance variables, 8 properties, 23 instance methods, 2 class methods

## Instance variables

```
@"MLStateConstraint" _stateConstraintCached;
B _optional;
@"NSString" _name;
q _type;
@"NSDictionary" _valueConstraints;
@"MLMultiArrayConstraint" _multiArrayConstraintCached;
@"MLImageConstraint" _imageConstraintCached;
@"MLDictionaryConstraint" _dictionaryConstraintCached;
@"MLSequenceConstraint" _sequenceConstraintCached;
```

## Properties

```
@property (T@"NSDictionary",&,V_valueConstraints) valueConstraints;
@property (T@"MLMultiArrayConstraint",R,N,V_multiArrayConstraintCached) multiArrayConstraintCached;
@property (T@"MLImageConstraint",R,N,V_imageConstraintCached) imageConstraintCached;
@property (T@"MLDictionaryConstraint",R,N,V_dictionaryConstraintCached) dictionaryConstraintCached;
@property (T@"MLSequenceConstraint",R,N,V_sequenceConstraintCached) sequenceConstraintCached;
@property (T@"NSString",R,C,N,V_name) name;
@property (Tq,R,N,V_type) type;
@property (TB,R,N,GisOptional,V_optional) optional;
```

## Class methods

```
+[MLFeatureDescription supportsSecureCoding];
+[MLFeatureDescription featureDescriptionWithName:type:optional:constraints:];
```

## Instance methods

```
-[MLFeatureDescription dictionaryConstraint];
-[MLFeatureDescription initWithName:type:optional:contraints:];
-[MLFeatureDescription debugQuickLookObject];
-[MLFeatureDescription multiArrayConstraint];
-[MLFeatureDescription isOptional];
-[MLFeatureDescription sequenceConstraintCached];
-[MLFeatureDescription stateConstraint];
-[MLFeatureDescription setValueConstraints:];
-[MLFeatureDescription imageConstraint];
-[MLFeatureDescription sequenceConstraint];
-[MLFeatureDescription type];
-[MLFeatureDescription encodeWithCoder:];
-[MLFeatureDescription description];
-[MLFeatureDescription multiArrayConstraintCached];
-[MLFeatureDescription initWithCoder:];
-[MLFeatureDescription valueConstraints];
-[MLFeatureDescription allowsValuesWithDescription:];
-[MLFeatureDescription dictionaryConstraintCached];
-[MLFeatureDescription isAllowedValue:error:];
-[MLFeatureDescription copyWithZone:];
-[MLFeatureDescription isAllowedValue:];
-[MLFeatureDescription name];
-[MLFeatureDescription imageConstraintCached];
```
