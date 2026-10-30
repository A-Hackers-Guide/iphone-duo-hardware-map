# `CAFTrailingButtons`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSFastEnumeration`
- 2 instance variables, 4 properties, 9 instance methods, 2 class methods

## Instance variables

```
@"NSArray" _trailingButtons;
@"NSError" _parseError;
```

## Properties

```
@property (T@"NSArray",R,N,V_trailingButtons) trailingButtons;
@property (T@"NSError",R,N,V_parseError) parseError;
@property (T@"NSString",R,N) formattedValue;
@property (T@"NSArray",R,N) arrayRepresentation;
```

## Class methods

```
+[CAFTrailingButtons trailingButtonsWithArray:];
+[CAFTrailingButtons trailingButtonsWithTrailingButtons:];
```

## Instance methods

```
-[CAFTrailingButtons formattedValue];
-[CAFTrailingButtons objectAtIndexedSubscript:];
-[CAFTrailingButtons initWithArray:];
-[CAFTrailingButtons countByEnumeratingWithState:objects:count:];
-[CAFTrailingButtons arrayRepresentation];
-[CAFTrailingButtons objectAtIndex:];
-[CAFTrailingButtons parseError];
-[CAFTrailingButtons trailingButtons];
-[CAFTrailingButtons initWithTrailingButtons:];
```
