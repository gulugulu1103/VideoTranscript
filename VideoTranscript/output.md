# 设计模式入门 - 简单工厂模式

设计模式是开发中常用的一种软件设计思想，它通过一种标准化的方式来解决一类问题。今天，我们将结合一个具体的例子来讲解简单工厂模式。

## 简单工厂模式

简单工厂模式是一种创建型模式，它通过一个单独的工厂类来创建不同类型的对象，而无需显示地指定它们的具体类。

### 场景示例

假设我们要为一个商场设计收银软件，收银员根据客户购买的商品单价和数量来收费，现在需要加入打折及促销的功能。

### 步骤1：问题分析

最初的软件可能仅仅通过单价和数量进行简单的乘法计算，但随着需求的发展，添加不同的折扣和促销方式，如果继续在原有基础上修改，代码将变得复杂且难以维护。

### 步骤2：简单工厂模式应用

我们引入简单工厂模式，通过工厂类来负责创建不同的折扣对象。

#### 创建收费父类

```python
class CashSuper:
    def accept_cash(self, money):
        pass
```

#### 创建具体的收费子类

```python
class CashNormal(CashSuper):
    def accept_cash(self, money):
        return money

class CashRebate(CashSuper):
    def __init__(self, discount):
        self.discount = discount

    def accept_cash(self, money):
        return money * self.discount

class CashReturn(CashSuper):
    def __init__(self, money_condition, money_return):
        self.money_condition = money_condition
        self.money_return = money_return

    def accept_cash(self, money):
        if money >= self.money_condition:
            return money - (money // self.money_condition) * self.money_return
        else:
            return money
```

#### 创建工厂类

```python
class CashFactory:
    def create_cash_accept(self, type):
        if type == 'normal':
            return CashNormal()
        elif type == 'rebate':
            return CashRebate(0.8)  # 举例：8折
        elif type == 'return':
            return CashReturn(300, 100)  # 举例：满300返100
```

### 步骤3：实际应用

假设我们现在要创建一个正常收费的对象：

```python
factory = CashFactory()
cash = factory.create_cash_accept('normal')
print(cash.accept_cash(1000))  # 输出1000，不打折
```

如果需求变更，要求打八折：

```python
cash = factory.create_cash_accept('rebate')
print(cash.accept_cash(1000))  # 输出800，打八折
```

### 步骤4：优点与改进

简单工厂模式的优点在于，将对象的创建和使用分离，有助于系统的解耦和扩展。但当有新的折扣方式加入时，依旧需要修改工厂类，违反了开闭原则。

为进一步优化代码，可以考虑策略模式，将变化的部分封装起来，增强系统的灵活性和可维护性。

## 小结

通过以上步骤，我们能够理解简单工厂模式的基本概念和应用场景，可以看出，设计模式能够帮助我们更好地组织和应对代码变更，但也需要根据实际情况选择合适的设计模式。

**记得实践！**实现几个具体的练习案例，比如针对不同类型的商品应用不同的折扣策略，或者针对特殊日子（如黑色星期五）应用特殊的促销策略。

_Happy Coding!_