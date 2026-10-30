# `SECSFAMatchProperty`

- Image: [`/System/Library/Frameworks/Security.framework/Security`](../userland/System__Library__Frameworks__Security.framework__Security.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 2 instance variables, 4 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"NSString" _propertyName;
@"SECSFAPropertyValue" _value;
```

## Properties

```
@property (TB,R,N) hasPropertyName;
@property (T@"NSString",&,N,V_propertyName) propertyName;
@property (TB,R,N) hasValue;
@property (T@"SECSFAPropertyValue",&,N,V_value) value;
```

## Instance methods

```
-[SECSFAMatchProperty writeTo:];
-[SECSFAMatchProperty mergeFrom:];
-[SECSFAMatchProperty propertyName];
-[SECSFAMatchProperty value];
-[SECSFAMatchProperty setValue:];
-[SECSFAMatchProperty hash];
-[SECSFAMatchProperty copyTo:];
-[SECSFAMatchProperty description];
-[SECSFAMatchProperty hasValue];
-[SECSFAMatchProperty readFrom:];
-[SECSFAMatchProperty copyWithZone:];
-[SECSFAMatchProperty isEqual:];
-[SECSFAMatchProperty dictionaryRepresentation];
-[SECSFAMatchProperty hasPropertyName];
-[SECSFAMatchProperty setPropertyName:];
```
