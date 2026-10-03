import torch
import os
import numpy as np
import typing, types
import torch.optim # for optimizers
import torch.nn as nn # for neural network modules
from typing import override
import torch.nn.functional as f # for non-linear function
from torch.utils.data import DataLoader, Dataset # for data handling

# Feedforward Neural Network Class
class fnn(nn.Module):

    prec: np.float1
    
    def __init__(self, prec: np.float16 | np.float32 | np.float64 | np.float96 | np.float128) -> None:
        
        super().__init__()


    # Backpropagation Algorithm
    def __backprop(self, inp: torch.Tensor, out: torch.Tensor):
        
        return torch.autograd.grad(inp, out)

    def fit(self, in_feat: int, out_feat: int, x_train: nn.Sequential, y_train: nn.Sequential, epoch_num: int):

        layers = nn.Sequential(
            nn.Linear(in_feat, out_feat),
            nn.ReLU(),
            nn.Linear(out_feat, in_feat),
            nn.ReLU(),
            nn.Linear(in_feat, out_feat),
            nn.ReLU(),
            nn.Linear(out_feat, in_feat)
        )

        for i in range(epoch_num):
            
            forward_pass = layers.forward
            print(forward_pass)
        
            backprop = self.__backprop(forward_pass)
            print(backprop)

            print(f"Training loss: {loss}")


    # Optimization Algorithm - SOON
        

    #Pass it to hidden layer torch.nn.function where it does sigmoid activation etc 

class cnn(nn.Module):

    prec: np.float1
    
    def __init__(self, prec: np.float16 | np.float32 | np.float64 | np.float96 | np.float128) -> None:
        
        super().__init__()


    # Backpropagation Algorithm
    def __backprop(self, inp: torch.Tensor, out: torch.Tensor):
        
        return torch.autograd.grad(inp, out)

    def fit(self, in_feat: int, out_feat: int, x_train: nn.Sequential, y_train: nn.Sequential, epoch_num: int):

        layers = nn.Sequential(
            nn.Linear(in_feat, out_feat),
            nn.ReLU(),
            nn.Linear(out_feat, in_feat),
            nn.ReLU(),
            nn.Linear(in_feat, out_feat),
            nn.ReLU(),
            nn.Linear(out_feat, in_feat)
        )

        for i in range(epoch_num):
            
            forward_pass = layers.forward
            print(forward_pass)
        
            backprop = self.__backprop(forward_pass)
            print(backprop)

            print(f"Training loss: {loss}")


    # Optimization Algorithm - SOON
        

    #Pass it to hidden layer torch.nn.function where it does sigmoid activation etc 

class rnn(nn.Module):

    prec: np.float1
    
    def __init__(self, prec: np.float16 | np.float32 | np.float64 | np.float96 | np.float128) -> None:
        
        super().__init__()


    # Backpropagation Algorithm
    def __backprop(self, inp: torch.Tensor, out: torch.Tensor):
        
        return torch.autograd.grad(inp, out)

    def fit(self, in_feat: int, out_feat: int, x_train: nn.Sequential, y_train: nn.Sequential, epoch_num: int):

        layers = nn.Sequential(
            nn.Linear(in_feat, out_feat),
            nn.ReLU(),
            nn.Linear(out_feat, in_feat),
            nn.ReLU(),
            nn.Linear(in_feat, out_feat),
            nn.ReLU(),
            nn.Linear(out_feat, in_feat)
        )

        for i in range(epoch_num):
            
            forward_pass = layers.forward
            print(forward_pass)
        
            backprop = self.__backprop(forward_pass)
            print(backprop)

            print(f"Training loss: {loss}")


    # Optimization Algorithm - SOON
        

    #Pass it to hidden layer torch.nn.function where it does sigmoid activation etc 

class gan(nn.Module):

    prec: np.float1
    
    def __init__(self, prec: np.float16 | np.float32 | np.float64 | np.float96 | np.float128) -> None:
        
        super().__init__()


    # Backpropagation Algorithm
    def __backprop(self, inp: torch.Tensor, out: torch.Tensor):
        
        return torch.autograd.grad(inp, out)

    def fit(self, in_feat: int, out_feat: int, x_train: nn.Sequential, y_train: nn.Sequential, epoch_num: int):

        layers = nn.Sequential(
            nn.Linear(in_feat, out_feat),
            nn.ReLU(),
            nn.Linear(out_feat, in_feat),
            nn.ReLU(),
            nn.Linear(in_feat, out_feat),
            nn.ReLU(),
            nn.Linear(out_feat, in_feat)
        )

        for i in range(epoch_num):
            
            forward_pass = layers.forward
            print(forward_pass)
        
            backprop = self.__backprop(forward_pass)
            print(backprop)

            print(f"Training loss: {loss}")


    # Optimization Algorithm - SOON
        

    #Pass it to hidden layer torch.nn.function where it does sigmoid activation etc 

class lstm(nn.Module):

    prec: np.float1
    
    def __init__(self, prec: np.float16 | np.float32 | np.float64 | np.float96 | np.float128) -> None:
        
        super().__init__()


    # Backpropagation Algorithm
    def __backprop(self, inp: torch.Tensor, out: torch.Tensor):
        
        return torch.autograd.grad(inp, out)

    def fit(self, in_feat: int, out_feat: int, x_train: nn.Sequential, y_train: nn.Sequential, epoch_num: int):

        layers = nn.Sequential(
            nn.Linear(in_feat, out_feat),
            nn.ReLU(),
            nn.Linear(out_feat, in_feat),
            nn.ReLU(),
            nn.Linear(in_feat, out_feat),
            nn.ReLU(),
            nn.Linear(out_feat, in_feat)
        )

        for i in range(epoch_num):
            
            forward_pass = layers.forward
            print(forward_pass)
        
            backprop = self.__backprop(forward_pass)
            print(backprop)

            print(f"Training loss: {loss}")


    # Optimization Algorithm - SOON
        

    #Pass it to hidden layer torch.nn.function where it does sigmoid activation etc 

class transf(nn.Module):

    prec: np.float1
    
    def __init__(self, prec: np.float16 | np.float32 | np.float64 | np.float96 | np.float128) -> None:
        
        super().__init__()


    # Backpropagation Algorithm
    def __backprop(self, inp: torch.Tensor, out: torch.Tensor):
        
        return torch.autograd.grad(inp, out)

    def fit(self, in_feat: int, out_feat: int, x_train: nn.Sequential, y_train: nn.Sequential, epoch_num: int):

        layers = nn.Sequential(
            nn.Linear(in_feat, out_feat),
            nn.ReLU(),
            nn.Linear(out_feat, in_feat),
            nn.ReLU(),
            nn.Linear(in_feat, out_feat),
            nn.ReLU(),
            nn.Linear(out_feat, in_feat)
        )

        for i in range(epoch_num):
            
            forward_pass = layers.forward
            print(forward_pass)
        
            backprop = self.__backprop(forward_pass)
            print(backprop)

            print(f"Training loss: {loss}")


    # Optimization Algorithm - SOON
        

    #Pass it to hidden layer torch.nn.function where it does sigmoid activation etc 