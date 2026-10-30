# `FigHUDGraphLayer`

- Image: [`/System/Library/Frameworks/MediaToolbox.framework/MediaToolbox`](../userland/System__Library__Frameworks__MediaToolbox.framework__MediaToolbox.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CALayer`
- 11 instance variables, 0 properties, 7 instance methods, 0 class methods

## Instance variables

```
^^f _Values;
@"NSMutableArray" _valueLabels;
^f _Mins;
^f _Maxes;
^i _StartIndex;
^i _NumValues;
i _NumGraphs;
^{CGPoint=dd} _Lines;
i _MaxLength;
^{__CTFont=} _Font;
^{__CFDictionary=} _TextAttributes;
```

## Instance methods

```
-[FigHUDGraphLayer drawInContext:];
-[FigHUDGraphLayer init];
-[FigHUDGraphLayer dealloc];
-[FigHUDGraphLayer setUpGraph:min:max:numValues:];
-[FigHUDGraphLayer setUpGraphs:];
-[FigHUDGraphLayer updateValue:value:];
-[FigHUDGraphLayer updateValue:value:label:];
```
