-- MySQL Script generated by MySQL Workbench
-- Чт 31 окт 2019 16:39:52
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`Teams`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Teams` (
  `id` INT NOT NULL,
  `name` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`MarkName`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`MarkName` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`TimeMarks`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`TimeMarks` (
  `id` INT NOT NULL,
  `mark` TIME NULL DEFAULT NULL,
  `id_Teams` INT NOT NULL,
  `id_MarkName` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_TimeMarks_Teams_idx` (`id_Teams` ASC),
  INDEX `fk_TimeMarks_MarkName1_idx` (`id_MarkName` ASC),
  CONSTRAINT `fk_TimeMarks_Teams`
    FOREIGN KEY (`id_Teams`)
    REFERENCES `mydb`.`Teams` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_TimeMarks_MarkName1`
    FOREIGN KEY (`id_MarkName`)
    REFERENCES `mydb`.`MarkName` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
