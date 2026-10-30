# `CAFProminenceInfo`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSFastEnumeration`
- 2 instance variables, 4 properties, 9 instance methods, 2 class methods

## Instance variables

```
@"NSArray" _prominenceInformations;
@"NSError" _parseError;
```

## Properties

```
@property (T@"NSArray",R,N,V_prominenceInformations) prominenceInformations;
@property (T@"NSError",R,N,V_parseError) parseError;
@property (T@"NSString",R,N) formattedValue;
@property (T@"NSArray",R,N) arrayRepresentation;
```

## Class methods

```
+[CAFProminenceInfo prominenceInfoWithArray:];
+[CAFProminenceInfo prominenceInfoWithProminenceInformations:];
```

## Instance methods

```
-[CAFProminenceInfo formattedValue];
-[CAFProminenceInfo objectAtIndexedSubscript:];
-[CAFProminenceInfo initWithArray:];
-[CAFProminenceInfo countByEnumeratingWithState:objects:count:];
-[CAFProminenceInfo arrayRepresentation];
-[CAFProminenceInfo objectAtIndex:];
-[CAFProminenceInfo parseError];
-[CAFProminenceInfo initWithProminenceInformations:];
-[CAFProminenceInfo prominenceInformations];
```
