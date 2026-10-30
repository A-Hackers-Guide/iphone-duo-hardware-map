# `SECSFAPropertyValue`

- Image: [`/System/Library/Frameworks/Security.framework/Security`](../userland/System__Library__Frameworks__Security.framework__Security.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 4 instance variables, 6 properties, 23 instance methods, 0 class methods

## Instance variables

```
q _integer;
i _property;
@"NSString" _string;
{?="integer"b1"property"b1} _has;
```

## Properties

```
@property (TB,N) hasInteger;
@property (Tq,N,V_integer) integer;
@property (TB,R,N) hasString;
@property (T@"NSString",&,N,V_string) string;
@property (TB,N) hasProperty;
@property (Ti,N,V_property) property;
```

## Instance methods

```
-[SECSFAPropertyValue property];
-[SECSFAPropertyValue setProperty:];
-[SECSFAPropertyValue writeTo:];
-[SECSFAPropertyValue mergeFrom:];
-[SECSFAPropertyValue string];
-[SECSFAPropertyValue setString:];
-[SECSFAPropertyValue hash];
-[SECSFAPropertyValue copyTo:];
-[SECSFAPropertyValue description];
-[SECSFAPropertyValue readFrom:];
-[SECSFAPropertyValue copyWithZone:];
-[SECSFAPropertyValue isEqual:];
-[SECSFAPropertyValue dictionaryRepresentation];
-[SECSFAPropertyValue StringAsProperty:];
-[SECSFAPropertyValue integer];
-[SECSFAPropertyValue setHasProperty:];
-[SECSFAPropertyValue clearOneofValuesForProperty];
-[SECSFAPropertyValue hasInteger];
-[SECSFAPropertyValue hasProperty];
-[SECSFAPropertyValue hasString];
-[SECSFAPropertyValue propertyAsString:];
-[SECSFAPropertyValue setHasInteger:];
-[SECSFAPropertyValue setInteger:];
```
