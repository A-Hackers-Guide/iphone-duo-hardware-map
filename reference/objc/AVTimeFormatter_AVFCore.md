# `AVTimeFormatter`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSFormatter`
- 1 instance variables, 3 properties, 28 instance methods, 0 class methods

## Instance variables

```
@"AVTimeFormatterInternal" _internal;
```

## Properties

```
@property (Tq,N) style;
@property (Td,N) formatTemplate;
@property (TB,N,GisFullWidth) fullWidth;
```

## Instance methods

```
-[AVTimeFormatter stringForObjectValue:];
-[AVTimeFormatter init];
-[AVTimeFormatter setFormatTemplate:];
-[AVTimeFormatter isFullWidth];
-[AVTimeFormatter setFullWidth:];
-[AVTimeFormatter stringFromCMTime:];
-[AVTimeFormatter dealloc];
-[AVTimeFormatter setLocale:];
-[AVTimeFormatter setCachedDateFormatterFormat:];
-[AVTimeFormatter style];
-[AVTimeFormatter setStyle:];
-[AVTimeFormatter isRightToLeft];
-[AVTimeFormatter stringFromTimeInterval:];
-[AVTimeFormatter setNumberFormatterWithOneMinimumIntegerDigits:];
-[AVTimeFormatter locale];
-[AVTimeFormatter formatTemplate];
-[AVTimeFormatter encodeWithCoder:];
-[AVTimeFormatter cachedDateFormatterTemplate];
-[AVTimeFormatter setIsRightToLeft:];
-[AVTimeFormatter initWithCoder:];
-[AVTimeFormatter getObjectValue:forString:errorDescription:];
-[AVTimeFormatter cachedDateFormatterFormat];
-[AVTimeFormatter copyWithZone:];
-[AVTimeFormatter numberFormatterWithTwoMinimumIntegerDigits];
-[AVTimeFormatter setCachedDateFormatterTemplate:];
-[AVTimeFormatter numberFormatterWithOneMinimumIntegerDigits];
-[AVTimeFormatter setNumberFormatterWithTwoMinimumIntegerDigits:];
-[AVTimeFormatter stringFromSeconds:];
```
