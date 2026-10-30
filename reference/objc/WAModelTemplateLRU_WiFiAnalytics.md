# `WAModelTemplateLRU`

- Image: [`/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics`](../userland/System__Library__PrivateFrameworks__WiFiAnalytics.framework__WiFiAnalytics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 4 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _keyToTemplate;
@"NSMutableDictionary" _keyToEncodedSize;
@"NSMutableOrderedSet" _lruOrder;
Q _totalEncodedBytes;
Q _budgetEncodedBytes;
Q _evictionCount;
```

## Properties

```
@property (TQ,R,N) entryCount;
@property (TQ,R,N) totalEncodedBytes;
@property (TQ,R,N) evictionCount;
@property (TQ,R,N) budgetEncodedBytes;
```

## Instance methods

```
-[WAModelTemplateLRU removeAllObjects];
-[WAModelTemplateLRU entryCount];
-[WAModelTemplateLRU evictionCount];
-[WAModelTemplateLRU setTemplate:forKey:encodedSize:];
-[WAModelTemplateLRU templateForKey:];
-[WAModelTemplateLRU _removeKey:];
-[WAModelTemplateLRU budgetEncodedBytes];
-[WAModelTemplateLRU initWithBudgetBytes:];
-[WAModelTemplateLRU totalEncodedBytes];
```
