-- MySQL Script generated by MySQL Workbench
-- Вт 29 окт 2019 12:13:43
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema turGaddb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema turGaddb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `turGaddb` ;
USE `turGaddb` ;

-- -----------------------------------------------------
-- Table `turGaddb`.`Teams`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `turGaddb`.`Teams` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `turGaddb`.`MarkName`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `turGaddb`.`MarkName` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `turGaddb`.`TimeMarks`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `turGaddb`.`TimeMarks` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `mark` TIME NOT NULL,
  `id_Team` INT NOT NULL,
  `id_MarkName` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_TimeMarks_Teams_idx` (`id_Team` ASC) VISIBLE,
  INDEX `fk_TimeMarks_MarkName1_idx` (`id_MarkName` ASC) VISIBLE,
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE,
  CONSTRAINT `fk_TimeMarks_Teams`
    FOREIGN KEY (`id_Team`)
    REFERENCES `turGaddb`.`Teams` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_TimeMarks_MarkName1`
    FOREIGN KEY (`id_MarkName`)
    REFERENCES `turGaddb`.`MarkName` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
