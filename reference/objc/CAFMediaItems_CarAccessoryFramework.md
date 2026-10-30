# `CAFMediaItems`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSFastEnumeration`
- 2 instance variables, 4 properties, 9 instance methods, 2 class methods

## Instance variables

```
@"NSArray" _mediaItems;
@"NSError" _parseError;
```

## Properties

```
@property (T@"NSArray",R,N,V_mediaItems) mediaItems;
@property (T@"NSError",R,N,V_parseError) parseError;
@property (T@"NSString",R,N) formattedValue;
@property (T@"NSArray",R,N) arrayRepresentation;
```

## Class methods

```
+[CAFMediaItems mediaItemsWithArray:];
+[CAFMediaItems mediaItemsWithMediaItems:];
```

## Instance methods

```
-[CAFMediaItems mediaItems];
-[CAFMediaItems formattedValue];
-[CAFMediaItems objectAtIndexedSubscript:];
-[CAFMediaItems initWithArray:];
-[CAFMediaItems countByEnumeratingWithState:objects:count:];
-[CAFMediaItems arrayRepresentation];
-[CAFMediaItems objectAtIndex:];
-[CAFMediaItems parseError];
-[CAFMediaItems initWithMediaItems:];
```
